#!/usr/bin/env python3
"""Turn numbered source files in the repository root into LeetCode problem folders.

Input examples:
    1.cpp
    42.py
    3665.cpp

Output example:
    problems/1-two-sum/README.md
    problems/1-two-sum/solution.cpp

Only source files listed in the generated manifest are eligible for deletion by
 the GitHub Actions workflow. Failed problems are left untouched.
"""

from __future__ import annotations

import html
import re
import shutil
import sys
import tempfile
import time
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any

import requests


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parents[2]
PROBLEMS_DIR = ROOT_DIR / "problems"

# GitHub Actions checks this exact path before removing successfully processed
# root-level source files. The manifest lives in .git and is never committed.
GIT_DIR = ROOT_DIR / ".git"
if GIT_DIR.is_dir():
    MANIFEST_PATH = GIT_DIR / "leetcode_processed_solutions.txt"
else:
    # Useful for linked worktrees or non-standard local Git layouts.
    MANIFEST_PATH = ROOT_DIR / ".github" / "scripts" / ".processed_solutions.txt"

# LeetCode's public website GraphQL endpoint is the primary source. The
# community API is used only as a fallback if GraphQL is unavailable.
GRAPHQL_URL = "https://leetcode.com/graphql/"
FALLBACK_API_URL = "https://leetcode-api-pied.vercel.app"

HTTP_TIMEOUT = (10, 35)  # connect timeout, read timeout
MAX_ATTEMPTS = 4
BASE_RETRY_SECONDS = 2
MAX_RETRY_SECONDS = 30
QUESTION_PAGE_SIZE = 1000

RETRYABLE_STATUS_CODES = {408, 425, 429, 500, 502, 503, 504}

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