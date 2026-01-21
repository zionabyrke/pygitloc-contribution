import os
from typing import List

EXCLUDED_DIRS = {
    ".git",
    "node_modules",
    ".venv",
    "__pycache__",
}

def find_git_repos(base_path: str) -> List[str]:
    repos = []

    for root, dirs, _ in os.walk(base_path):
        # prune excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        git_path = os.path.join(root, ".git")
        if os.path.isdir(git_path):
            repos.append(root)
            dirs.clear()  # do not recurse further into this repo

    return repos
