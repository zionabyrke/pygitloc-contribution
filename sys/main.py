import os
from scanner import find_git_repos
from storage import load_repos, save_repos
from commits import collect_commits

# test finding repos
# pwd = os.getcwd()
# print(pwd)

directory = "C://Users//Renz//Documents"
# print(*find_git_repos(directory), sep='\n')

email = "renzkirbyonia@gmail.com"
repo = "C://Users//Renz//Documents//CODECRAFTERS//codecrafters-shell-cpp"
commits = collect_commits(repo, email)

print(f"Repo: {repo}")
if not repo:
    print("None found")

print(f"Found {len(commits)} commits")