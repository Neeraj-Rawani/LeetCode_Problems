import html
import re
import shutil
import unicodedata
from pathlib import Path

import requests


# =========================================================
# CONFIG
# =========================================================

ROOT_DIR = Path(".")
PROBLEMS_DIR = ROOT_DIR / "problems"

API_URL = "https://leetcode-api-pied.vercel.app"


# Files that should NEVER be treated as a solution.
# Any other root-level file like 123.py, 123.java, 123.go,
# 123.rs, 123.sql, 123.html, 123.css, etc. can be processed.
IGNORED_EXTENSIONS = {
    ".md",
    ".txt",
    ".json",
    ".jsonc",
    ".yaml",
    ".yml",
    ".toml",
    ".ini",
    ".cfg",
    ".conf",
    ".xml",
    ".csv",
    ".tsv",
    ".lock",
    ".log",
    ".map",
    ".ipynb",
}

IGNORED_FILENAMES = {
    "README",
    "LICENSE",
    "CHANGELOG",
    "CONTRIBUTING",
    "CODEOWNERS",
}


# =========================================================
# HTTP SESSION
# =========================================================

SESSION = requests.Session()

SESSION.headers.update(
    {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
    }
)


# =========================================================
# GENERAL HELPERS
# =========================================================

def get_value(data: dict, *keys, default=None):
    for key in keys:
        value = data.get(key)

        if value not in (None, "", []):
            return value

    return default


def slugify(title: str) -> str:
    title = html.unescape(
        str(title)
    )

    title = unicodedata.normalize(
        "NFKD",
        title
    ).encode(
        "ascii",
        "ignore"
    ).decode(
        "ascii"
    )

    title = title.lower().strip()

    title = re.sub(
        r"[^a-z0-9]+",
        "-",
        title
    )

    title = re.sub(
        r"-+",
        "-",
        title
    )

    return title.strip("-")


def extract_slug(question: dict) -> str:

    slug = get_value(
        question,
        "titleSlug",
        "title_slug",
        "slug"
    )

    if slug:
        return str(slug).strip("/")


    # Try URLs
    for key in (
        "url",
        "link",
        "problem_url",
        "questionUrl",
    ):

        value = question.get(key)

        if not value:
            continue

        match = re.search(
            r"/problems/([^/?#]+)",
            str(value)
        )

        if match:
            return match.group(1)


    # Generate from title
    title = get_value(
        question,
        "title",
        default=""
    )

    if title:
        return slugify(title)


    return f"problem-{question.get('questionFrontendId', 'unknown')}"


# =========================================================
# LANGUAGE DETECTION
# =========================================================

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
    ".R": "R",

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

    ".ex": "Elixir",

    ".rkt": "Racket",

    ".ml": "OCaml",
    ".mli": "OCaml",

    ".v": "V",

    ".hx": "Haxe",

    ".tcl": "Tcl",

    ".awk": "AWK",

    ".fth": "Forth",
}


def detect_language(file: Path) -> str:

    extension = file.suffix.lower()

    if extension in LANGUAGE_MAP:
        return LANGUAGE_MAP[extension]

    if extension:
        return extension[1:].upper()

    return "Unknown"


# =========================================================
# FIND ROOT SOLUTION FILES
# =========================================================

def get_solution_files():

    files = []

    for file in ROOT_DIR.iterdir():

        # Must be an actual file
        if not file.is_file():
            continue

        # Must have extension
        if not file.suffix:
            continue

        # Ignore known non-solution files
        if file.suffix.lower() in {
            ext.lower()
            for ext in IGNORED_EXTENSIONS
        }:
            continue

        # Filename must be ONLY a number before extension
        #
        # 2267.cpp     ✅
        # 1614.py      ✅
        # 100.java     ✅
        # abc.cpp      ❌
        # 2267-test.cpp ❌
        #
        if not re.fullmatch(
            r"\d+",
            file.stem
        ):
            continue

        # Ignore special filenames if ever encountered
        if file.stem.upper() in {
            name.upper()
            for name in IGNORED_FILENAMES
        }:
            continue

        files.append(file)

    return sorted(
        files,
        key=lambda file: int(
            file.stem
        )
    )


# =========================================================
# FETCH LEETCODE
# =========================================================

def fetch_problem(number: str):

    url = (
        f"{API_URL}/problem/{number}"
    )

    print(
        f"Fetching LeetCode #{number}..."
    )

    response = SESSION.get(
        url,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    if not isinstance(
        data,
        dict
    ):
        raise RuntimeError(
            "Invalid API response."
        )


    # Handle wrapped responses
    if isinstance(
        data.get("data"),
        dict
    ):

        if isinstance(
            data["data"].get("question"),
            dict
        ):

            data = data["data"]["question"]

        elif isinstance(
            data["data"].get("problem"),
            dict
        ):

            data = data["data"]["problem"]


    if not data.get(
        "title"
    ):

        raise RuntimeError(
            f"LeetCode #{number} was not found."
        )

    return data


# =========================================================
# CLEAN LEETCODE HTML
# =========================================================

def clean_problem_html(
    content: str
) -> str:

    if not content:
        return (
            "Problem description unavailable."
        )


    # Decode entities repeatedly
    for _ in range(5):

        decoded = html.unescape(
            content
        )

        if decoded == content:
            break

        content = decoded


    # Remove escaping before HTML tags
    content = re.sub(
        r"\\+(?=<\/?[A-Za-z])",
        "",
        content
    )


    # Remove escaping of Markdown characters
    content = re.sub(
        r"\\+(?=[`*_[\]()#<>])",
        "",
        content
    )


    # Fix malformed image source
    #
    # src="[https://abc](https://abc)"
    #
    # ->
    #
    # src="https://abc"
    content = re.sub(
        r'src\s*=\s*"\[(https?://[^\]]+)\]\([^)]+\)"',
        r'src="\1"',
        content,
        flags=re.IGNORECASE
    )

    content = re.sub(
        r"src\s*=\s*'\[(https?://[^\]]+)\]\([^)]+\)'",
        r"src='\1'",
        content,
        flags=re.IGNORECASE
    )


    # Fix malformed href
    content = re.sub(
        r'href\s*=\s*"\[(https?://[^\]]+)\]\([^)]+\)"',
        r'href="\1"',
        content,
        flags=re.IGNORECASE
    )

    content = re.sub(
        r"href\s*=\s*'\[(https?://[^\]]+)\]\([^)]+\)'",
        r"href='\1'",
        content,
        flags=re.IGNORECASE
    )


    # Example headings
    content = re.sub(
        r"<p>\s*"
        r"<strong[^>]*class=[\"'][^\"']*example[^\"']*[\"'][^>]*>"
        r"\s*Example\s+(\d+)\s*:?\s*"
        r"</strong>\s*</p>",
        r"<h3>Example \1</h3>",
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    content = re.sub(
        r"<strong[^>]*class=[\"'][^\"']*example[^\"']*[\"'][^>]*>"
        r"\s*Example\s+(\d+)\s*:?\s*"
        r"</strong>",
        r"<h3>Example \1</h3>",
        content,
        flags=re.IGNORECASE
    )


    # Constraints heading
    content = re.sub(
        r"<p>\s*"
        r"<strong[^>]*>\s*Constraints\s*:?\s*</strong>"
        r"\s*</p>",
        "<h2>Constraints</h2>",
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    content = re.sub(
        r"<strong[^>]*>\s*Constraints\s*:?\s*</strong>",
        "<h2>Constraints</h2>",
        content,
        flags=re.IGNORECASE
    )


    # Remove empty paragraphs
    content = re.sub(
        r"<p>\s*(?:&nbsp;|\u00a0|\s)*</p>",
        "",
        content,
        flags=re.IGNORECASE
    )


    # Normalize image tags
    def clean_image(match):

        attrs = match.group(1)

        src_match = re.search(
            r'src\s*=\s*["\']([^"\']+)["\']',
            attrs,
            flags=re.IGNORECASE
        )

        alt_match = re.search(
            r'alt\s*=\s*["\']([^"\']*)["\']',
            attrs,
            flags=re.IGNORECASE
        )

        style_match = re.search(
            r'style\s*=\s*["\']([^"\']*)["\']',
            attrs,
            flags=re.IGNORECASE
        )

        if not src_match:
            return match.group(0)

        src = src_match.group(1)

        alt = (
            alt_match.group(1)
            if alt_match
            else ""
        )

        width = None

        style = (
            style_match.group(1)
            if style_match
            else ""
        )

        width_match = re.search(
            r"width\s*:\s*(\d+)px",
            style,
            flags=re.IGNORECASE
        )

        if width_match:
            width = width_match.group(1)


        if width:

            return (
                f'<img src="{src}" '
                f'width="{width}" '
                f'alt="{alt}" />'
            )

        return (
            f'<img src="{src}" '
            f'alt="{alt}" />'
        )


    content = re.sub(
        r"<img\s+([^>]*?)\/?>",
        clean_image,
        content,
        flags=re.IGNORECASE
    )


    # Normalize line endings
    content = content.replace(
        "\r\n",
        "\n"
    )

    content = content.replace(
        "\r",
        "\n"
    )


    # Remove excessive blank lines
    content = re.sub(
        r"\n{4,}",
        "\n\n\n",
        content
    )


    return content.strip()


# =========================================================
# TOPICS
# =========================================================

def extract_topics(
    question: dict
):

    topics = get_value(
        question,
        "topicTags",
        "topics",
        "tags",
        default=[]
    )

    if not isinstance(
        topics,
        list
    ):
        return []


    result = []

    for topic in topics:

        if isinstance(
            topic,
            dict
        ):

            name = (
                topic.get("name")
                or topic.get("title")
                or topic.get("slug")
            )

        else:

            name = str(
                topic
            )


        if name:

            name = str(
                name
            )

            if name not in result:
                result.append(
                    name
                )


    return result


# =========================================================
# README
# =========================================================

def create_readme(
    question: dict,
    solution_file: Path
):

    number = get_value(
        question,
        "questionFrontendId",
        "frontendQuestionId",
        "questionId",
        "id",
        default=solution_file.stem
    )

    title = get_value(
        question,
        "title",
        default="Unknown Title"
    )

    difficulty = get_value(
        question,
        "difficulty",
        default="Unknown"
    )

    content = get_value(
        question,
        "content",
        "description",
        "problem",
        "translatedContent",
        default=""
    )

    content = clean_problem_html(
        str(content)
    )


    slug = extract_slug(
        question
    )


    problem_url = (
        f"https://leetcode.com/problems/"
        f"{slug}/"
    )


    topics = extract_topics(
        question
    )


    language = detect_language(
        solution_file
    )


    if topics:

        topic_text = "\n".join(
            f"- {topic}"
            for topic in topics
        )

    else:

        topic_text = (
            "- Not available"
        )


    return (
        f"# {number}. {title}\n\n"

        f"**Difficulty:** {difficulty}\n\n"

        f"**LeetCode:** "
        f"[Open Problem]({problem_url})\n\n"

        f"---\n\n"

        f"## Problem Description\n\n"

        f"{content}\n\n"

        f"---\n\n"

        f"## Topics\n\n"

        f"{topic_text}\n\n"

        f"---\n\n"

        f"## My Solution\n\n"

        f"**Language:** {language}\n\n"

        f"[View Solution](./solution"
        f"{solution_file.suffix})\n\n"

        f"---\n"
    )


# =========================================================
# COPY SOLUTION
# =========================================================

def copy_solution(
    source: Path,
    destination: Path
):

    if not source.exists():

        raise FileNotFoundError(
            f"Solution file not found: "
            f"{source}"
        )


    if not source.is_file():

        raise RuntimeError(
            f"{source} is not a regular file."
        )


    destination.write_bytes(
        source.read_bytes()
    )


# =========================================================
# REMOVE OLD GENERATED FOLDERS
# =========================================================

def remove_old_generated_folders(
    number: str
):

    if not PROBLEMS_DIR.exists():
        return


    prefix = f"{number}-"

    for folder in PROBLEMS_DIR.iterdir():

        if not folder.is_dir():
            continue

        if folder.name.startswith(
            prefix
        ):

            print(
                f"Removing old folder: "
                f"{folder}"
            )

            shutil.rmtree(
                folder
            )


# =========================================================
# PROCESS ONE SOLUTION
# =========================================================

def process_solution(
    solution_file: Path
):

    number = solution_file.stem

    print(
        f"Processing LeetCode #{number}..."
    )


    # Fetch problem
    question = fetch_problem(
        number
    )


    # Get correct slug
    slug = extract_slug(
        question
    )


    # Remove previous generated folder
    remove_old_generated_folders(
        number
    )


    # Final problem directory
    problem_dir = (
        PROBLEMS_DIR
        / f"{number}-{slug}"
    )

    problem_dir.mkdir(
        parents=True,
        exist_ok=True
    )


    # Preserve original extension
    solution_destination = (
        problem_dir
        / f"solution{solution_file.suffix}"
    )


    # Copy solution
    copy_solution(
        solution_file,
        solution_destination
    )


    # Generate README
    readme_path = (
        problem_dir
        / "README.md"
    )

    readme_path.write_text(
        create_readme(
            question,
            solution_file
        ),
        encoding="utf-8"
    )


    print(
        f"Created: {problem_dir}"
    )


# =========================================================
# MAIN
# =========================================================

def main():

    PROBLEMS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    solutions = get_solution_files()


    if not solutions:

        print(
            "No numbered solution files found."
        )

        return


    print(
        f"Found {len(solutions)} solution file(s)."
    )


    for solution in solutions:

        process_solution(
            solution
        )


    print(
        "Done."
    )


if __name__ == "__main__":
    main()