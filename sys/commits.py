from collections import defaultdict
from datetime import datetime, timedelta, date
from typing import Dict, Set

from dulwich.repo import Repo
from dulwich.objects import Commit

DAYS_BACK = 183  # ~6 months

def collect_commits(repo_path: str, email: str) -> Dict[date, int]:
    repo = Repo(repo_path)
    since = datetime.utcnow() - timedelta(days=DAYS_BACK)

    # initializations
    daily_counts: Dict[date, int] = defaultdict(int)
    seen_commits: Set[bytes] = set()

    for ref in repo.get_refs().values():
        try:
            obj = repo[ref]
        except KeyError:
            continue

        stack = [obj]
        while stack:
            commit = stack.pop()
            if not isinstance(commit, Commit):
                continue # if invalid

            if commit.id in seen_commits: # tracks commits in bytes
                continue
            seen_commits.add(commit.id)

            authored_time = datetime.utcfromtimestamp(commit.commit_time)
            if authored_time < since: 
                continue # skips not within timeframe

            author = commit.author.decode("utf-8", errors="ignore")
            if f"<{email}>" in author: # compare str to utf-8
                daily_counts[authored_time.date()] += 1 # tallying

            for parent in commit.parents:
                try:
                    stack.append(repo[parent])
                except KeyError:
                    continue

    return dict(daily_counts)
