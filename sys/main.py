import os
from scanner import find_git_repos

# test finding repos
# pwd = os.getcwd()
# print(pwd)

directory = "C://Users//Renz//Documents"
print(*find_git_repos(directory), sep='\n')