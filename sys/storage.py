from pathlib import Path
from typing import Set, Iterable
# Set = unordered unique tuples
# Iterable(str) = string tuples

DB_FILE = Path("repos.txt")

def load_repos() -> Set[str]:
    if not DB_FILE.exists():
        return set()
    return { # a Set of repos
        line.strip()
        for line in DB_FILE.read_text().splitlines()
        if line.strip()
    }

def save_repos(new_repos: Iterable[str]) -> None:
    repos = load_repos()
    repos.update(new_repos)
    DB_FILE.write_text("\n".join(sorted(repos)))
