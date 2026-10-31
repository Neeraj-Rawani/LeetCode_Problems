from __future__ import annotations

import html
import re
import shutil
import time
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

# Keep the temporary manifest inside Git metadata so it never becomes a repo file.
GIT_METADATA_DIR = ROOT_DIR / ".git"
MANIFEST_PATH = (
    GIT_METADATA_DIR / "leetcode_processed_solutions.txt"
    if GIT_METADATA_DIR.is_dir()
    else ROOT_DIR / ".github" / "scripts" / ".processed_solutions.txt"
)

API_URL = "https://leetcode-api-pied.vercel.app"

# API requests are retried individually for temporary failures such as HTTP 504.
MAX_API_ATTEMPTS = 4
API_TIMEOUT = (10, 30)  # (connection timeout, response/read timeout)
BASE_RETRY_DELAY = 2
MAX_RETRY_DELAY = 30
MAX_RETRY_AFTER = 60
RETRYABLE_HTTP_STATUSES = {408, 425, 429, 500, 502, 503, 504}

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