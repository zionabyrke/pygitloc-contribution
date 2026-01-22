import argparse
from scanner import find_git_repos
from storage import load_repos, save_repos
from commits import collect_commits
from merge import merge_stats
from intensity import intensity_level
from heatmap import render_heatmap

parser = argparse.ArgumentParser()
parser.add_argument("--add", "-a", help="Scan folder for Git repos")
parser.add_argument("--email", "-e", help="Author email")
args = parser.parse_args()

if args.add:
    repos = find_git_repos(args.add)
    save_repos(repos)
    print(f"Added {len(repos)} repositories.")

elif args.email:
        stats = [
            collect_commits(repo, args.email)
            for repo in load_repos()
        ]
        merged = merge_stats(stats)
        render_heatmap(merged)

else:
    parser.print_help()
