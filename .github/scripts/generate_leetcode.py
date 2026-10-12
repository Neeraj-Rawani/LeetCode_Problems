from __future__ import annotations

import html
import re
import shutil
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any

import requests


# =========================================================
# CONFIG
# =========================================================

# This script is expected at .github/scripts/generate_leetcode.py.
# Find the checked-out repository root so root-level files like 1.cpp are found.
SCRIPT_PATH = Path(__file__).resolve()
ROOT_DIR = next(
    (parent for parent in SCRIPT_PATH.parents if (parent / ".git").exists()),
    SCRIPT_PATH.parents[2]
    if len(SCRIPT_PATH.parents) > 2
    and SCRIPT_PATH.parent.name == "scripts"
    and SCRIPT_PATH.parent.parent.name == ".github"
    else SCRIPT_PATH.parent,
)
PROBLEMS_DIR = ROOT_DIR / "problems"
# Keep the temporary manifest inside Git metadata so it never becomes a repository file.
GIT_METADATA_DIR = ROOT_DIR / ".git"
MANIFEST_PATH = (
    GIT_METADATA_DIR / "leetcode_processed_solutions.txt"
    if GIT_METADATA_DIR.is_dir()
    else ROOT_DIR / ".github" / "scripts" / ".processed_solutions.txt"
)
API_URL = "https://leetcode-api-pied.vercel.app"

# These extensions are metadata/configuration, not solution files.
IGNORED_EXTENSIONS = {
    ".md", ".txt", ".json", ".jsonc", ".yaml", ".yml", ".toml",
    ".ini", ".cfg", ".conf", ".xml", ".csv", ".tsv", ".lock",
    ".log", ".map", ".ipynb",
}

IGNORED_FILENAMES = {
    "README", "LICENSE", "CHANGELOG", "CONTRIBUTING", "CODEOWNERS",
}

LANGUAGE_MAP = {
    ".c": "C",
    ".h": "C Header",
    ".cc": "C++",
    ".cpp": "C++",
    ".cxx": "C++",
    ".hpp": "C++ Header",
    ".cs": "C#",
    ".java": "Java",
    ".kt": "Kotlin",
    ".kts": "Kotlin",
    ".py": "Python",
    ".pyw": "Python",
    ".js": "JavaScript",
    ".jsx": "JavaScript / React",
    ".mjs": "JavaScript",
    ".cjs": "JavaScript",
    ".ts": "TypeScript",
    ".tsx": "TypeScript / React",
    ".go": "Go",
    ".rs": "Rust",
    ".rb": "Ruby",
    ".php": "PHP",
    ".swift": "Swift",
    ".dart": "Dart",
    ".scala": "Scala",
    ".sc": "Scala",
    ".r": "R",
    ".jl": "Julia",
    ".lua": "Lua",
    ".pl": "Perl",
    ".pm": "Perl",
    ".sh": "Shell",
    ".bash": "Bash",
    ".zsh": "Zsh",
    ".fish": "Fish",
    ".ps1": "PowerShell",
    ".bat": "Batch",
    ".cmd": "Batch",
    ".sql": "SQL",
    ".html": "HTML",
    ".htm": "HTML",
    ".css": "CSS",
    ".scss": "SCSS",
    ".sass": "Sass",
    ".less": "Less",
    ".m": "Objective-C",
    ".mm": "Objective-C++",
    ".fs": "F#",
    ".fsx": "F#",
    ".vb": "Visual Basic",
    ".hs": "Haskell",
    ".lhs": "Haskell",
    ".ex": "Elixir",
    ".exs": "Elixir",
    ".erl": "Erlang",
    ".hrl": "Erlang",
    ".clj": "Clojure",
    ".cljs": "ClojureScript",
    ".groovy": "Groovy",
    ".asm": "Assembly",
    ".s": "Assembly",
    ".sol": "Solidity",
    ".v": "Verilog",
    ".sv": "SystemVerilog",
    ".vhd": "VHDL",
    ".vhdl": "VHDL",
    ".pro": "Prolog",
    ".pas": "Pascal",
    ".f": "Fortran",
    ".f90": "Fortran",
    ".f95": "Fortran",
    ".f03": "Fortran",
    ".f08": "Fortran",
    ".nim": "Nim",
    ".zig": "Zig",
    ".cr": "Crystal",
    ".rkt": "Racket",
    ".ml": "OCaml",
    ".mli": "OCaml",
    ".hx": "Haxe",
    ".tcl": "Tcl",
    ".awk": "AWK",
    ".fth": "Forth",
}

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
})


def get_value(data: dict[str, Any], *keys: str, default: Any = None) -> Any:
    """Return the first present, non-empty value from a dictionary."""
    for key in keys:
        value = data.get(key)
        if value is not None and value != "" and value != []:
            return value
    return default


def slugify(title: str) -> str:
    title = html.unescape(str(title))
    title = unicodedata.normalize("NFKD", title)
    title = title.encode("ascii", "ignore").decode("ascii")
    title = title.lower().strip()
    title = re.sub(r"[^a-z0-9]+", "-", title)
    return re.sub(r"-+", "-", title).strip("-")


def extract_slug(question: dict[str, Any]) -> str:
    slug = get_value(question, "titleSlug", "title_slug", "slug")
    if slug:
        return str(slug).strip("/")

    for key in ("url", "link", "problem_url", "questionUrl"):
        value = question.get(key)
        if value:
            match = re.search(r"/problems/([^/?#]+)", str(value))
            if match:
                return match.group(1)

    title = get_value(question, "title", default="")
    if title:
        return slugify(str(title))

    return f"problem-{question.get('questionFrontendId', 'unknown')}"


def detect_language(file: Path) -> str:
    extension = file.suffix.lower()
    if extension in LANGUAGE_MAP:
        return LANGUAGE_MAP[extension]
    return extension[1:].upper() if extension else "Unknown"


def get_solution_files() -> list[Path]:
    """Find root-level files named only with a problem number, e.g. 1.cpp."""
    files: list[Path] = []
    ignored_extensions = {ext.lower() for ext in IGNORED_EXTENSIONS}
    ignored_names = {name.upper() for name in IGNORED_FILENAMES}

    try:
        root_items = ROOT_DIR.iterdir()
        for file in root_items:
            if not file.is_file() or not file.suffix:
                continue
            # Accept only extensions whose language we explicitly support.
            # This avoids treating files such as 123.pdf or 123.exe as solutions.
            if file.suffix.lower() not in LANGUAGE_MAP:
                continue
            if file.suffix.lower() in ignored_extensions:
                continue
            if not re.fullmatch(r"\d+", file.stem):
                continue
            if file.stem.upper() in ignored_names:
                continue
            files.append(file)
    except OSError as exc:
        raise RuntimeError(f"Cannot read project root: {ROOT_DIR}\n{exc}") from exc

    return sorted(files, key=lambda file: (int(file.stem), file.suffix.lower()))


def fetch_problem(number: str) -> dict[str, Any]:
    url = f"{API_URL}/problem/{number}"
    print(f"  Fetching LeetCode #{number}...")

    try:
        response = SESSION.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
    except requests.Timeout as exc:
        raise RuntimeError("API request timed out. Check your internet and try again.") from exc
    except requests.HTTPError as exc:
        status = exc.response.status_code if exc.response is not None else "unknown"
        raise RuntimeError(f"API returned HTTP {status} for problem #{number}.") from exc
    except requests.RequestException as exc:
        raise RuntimeError(f"Could not connect to the LeetCode API: {exc}") from exc
    except ValueError as exc:
        raise RuntimeError("API response was not valid JSON.") from exc

    if not isinstance(data, dict):
        raise RuntimeError("API returned an unexpected response format (expected an object).")

    # Support both direct responses and common wrapped response shapes.
    for _ in range(3):
        nested = None
        for key in ("question", "problem"):
            candidate = data.get(key)
            if isinstance(candidate, dict) and candidate.get("title"):
                nested = candidate
                break
        if nested is None:
            wrapper = data.get("data")
            if isinstance(wrapper, dict):
                for key in ("question", "problem"):
                    candidate = wrapper.get(key)
                    if isinstance(candidate, dict) and candidate.get("title"):
                        nested = candidate
                        break
        if nested is None:
            break
        data = nested

    if not data.get("title"):
        detail = data.get("detail") or data.get("message") or "No problem title was returned"
        raise RuntimeError(f"LeetCode #{number} was not found. API says: {detail}")

    return data


def clean_problem_html(content: str) -> str:
    """Make small safe normalizations while retaining GitHub-renderable HTML."""
    if not content:
        return "Problem description unavailable."

    # Decode nested HTML entities, but do not strip the returned HTML structure.
    for _ in range(3):
        decoded = html.unescape(content)
        if decoded == content:
            break
        content = decoded

    # Remove escaping accidentally placed before HTML/Markdown punctuation.
    content = re.sub(r"\\(?=<\/?[A-Za-z])", "", content)
    content = re.sub(r"\\(?=[`*_#<>])", "", content)

    # Improve common headings found in LeetCode problem HTML.
    content = re.sub(
        r"<p>\s*<strong[^>]*>\s*Example\s+(\d+)\s*:?\s*</strong>\s*</p>",
        r"<h3>Example \1</h3>", content, flags=re.IGNORECASE | re.DOTALL,
    )
    content = re.sub(
        r"<strong[^>]*>\s*Example\s+(\d+)\s*:?\s*</strong>",
        r"<h3>Example \1</h3>", content, flags=re.IGNORECASE,
    )
    content = re.sub(
        r"<p>\s*<strong[^>]*>\s*Constraints\s*:?\s*</strong>\s*</p>",
        "<h2>Constraints</h2>", content, flags=re.IGNORECASE | re.DOTALL,
    )
    content = re.sub(
        r"<strong[^>]*>\s*Constraints\s*:?\s*</strong>",
        "<h2>Constraints</h2>", content, flags=re.IGNORECASE,
    )
    content = re.sub(
        r"<p>\s*(?:&nbsp;|\u00a0|\s)*</p>",
        "", content, flags=re.IGNORECASE,
    )

    content = content.replace("\r\n", "\n").replace("\r", "\n")
    content = re.sub(r"\n{4,}", "\n\n\n", content)
    return content.strip()


def extract_topics(question: dict[str, Any]) -> list[str]:
    topics = get_value(question, "topicTags", "topics", "tags", default=[])
    if not isinstance(topics, list):
        return []

    result: list[str] = []
    for topic in topics:
        if isinstance(topic, dict):
            name = topic.get("name") or topic.get("title") or topic.get("slug")
        else:
            name = str(topic)
        if name:
            name = str(name)
            if name not in result:
                result.append(name)
    return result


def create_readme(number: str, question: dict[str, Any], solution_files: list[Path]) -> str:
    title = get_value(question, "title", default="Unknown Title")
    difficulty = get_value(question, "difficulty", default="Unknown")
    description = get_value(
        question, "content", "description", "problem", "translatedContent", default=""
    )
    description = clean_problem_html(str(description))
    slug = extract_slug(question)
    problem_url = f"https://leetcode.com/problems/{slug}/"

    topics = extract_topics(question)
    topic_text = "\n".join(f"- {topic}" for topic in topics) if topics else "- Not available"

    solution_links = []
    for solution_file in solution_files:
        language = detect_language(solution_file)
        solution_links.append(
            f"- **{language}:** [View Solution](./solution{solution_file.suffix})"
        )

    solutions_text = "\n".join(solution_links)

    return (
        f"# {number}. {title}\n\n"
        f"**Difficulty:** {difficulty}\n\n"
        f"**LeetCode:** [Open Problem]({problem_url})\n\n"
        "---\n\n"
        "## Problem Description\n\n"
        f"{description}\n\n"
        "---\n\n"
        "## Topics\n\n"
        f"{topic_text}\n\n"
        "---\n\n"
        "## My Solution\n\n"
        f"{solutions_text}\n\n"
        "---\n"
    )


def process_problem(number: str, source_files: list[Path]) -> bool:
    print(f"Processing LeetCode #{number} ({len(source_files)} solution file(s))...")
    try:
        question = fetch_problem(number)
        slug = extract_slug(question)
        problem_dir = PROBLEMS_DIR / f"{number}-{slug}"
        problem_dir.mkdir(parents=True, exist_ok=True)

        # Copy all language variants for the same problem, e.g. 1.cpp and 1.py.
        copied_files: list[Path] = []
        for source in source_files:
            destination = problem_dir / f"solution{source.suffix}"
            shutil.copy2(source, destination)
            copied_files.append(source)

        readme_path = problem_dir / "README.md"
        # Remove stale generated solution files if the language/extension changed.
        expected_solution_names = {f"solution{source.suffix}" for source in source_files}
        for old_solution in problem_dir.glob("solution.*"):
            if old_solution.name not in expected_solution_names and old_solution.is_file():
                old_solution.unlink()

        readme_path.write_text(
            create_readme(number, question, copied_files),
            encoding="utf-8",
        )
        print(f"  Created/updated: {problem_dir.relative_to(ROOT_DIR)}")
        return True
    except Exception as exc:
        print(f"  ERROR for problem #{number}: {exc}")
        return False


def main() -> int:
    PROBLEMS_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Clear any stale manifest before processing this run.
    MANIFEST_PATH.write_text("", encoding="utf-8")
    solution_files = get_solution_files()

    if not solution_files:
        print(f"No numbered solution files found in: {ROOT_DIR}")
        print("Example accepted filenames: 1.cpp, 42.py, 2267.java")
        return 0

    # One API request per problem number, even when multiple languages are present.
    grouped: dict[str, list[Path]] = defaultdict(list)
    for file in solution_files:
        grouped[file.stem].append(file)

    print(f"Found {len(solution_files)} solution file(s) across {len(grouped)} problem(s).")
    succeeded = 0
    failed = 0
    successfully_processed: list[Path] = []

    for number, files_for_problem in sorted(grouped.items(), key=lambda item: int(item[0])):
        if process_problem(number, files_for_problem):
            succeeded += 1
            successfully_processed.extend(files_for_problem)
        else:
            failed += 1

    # The workflow uses this manifest instead of deleting every numeric filename.
    # Only fully processed source files are listed.
    manifest_text = "\n".join(
        file.relative_to(ROOT_DIR).as_posix()
        for file in successfully_processed
    )
    MANIFEST_PATH.write_text(
        manifest_text + ("\n" if manifest_text else ""),
        encoding="utf-8",
    )

    print(f"\nFinished. Successful problems: {succeeded}; failed problems: {failed}.")
    if failed:
        print("One or more problems failed. Source files will not be removed by the workflow.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
