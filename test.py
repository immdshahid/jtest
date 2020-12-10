
import os
from github import Github
import subprocess

# token = os.getenv('GITHUB_TOKEN', '800f2b5bc4a1d4b62a8f37e69abb7ecca3c00d1f')
g = Github('800f2b5bc4a1d4b62a8f37e69abb7ecca3c00d1f')
name= g.get_user('immdshahid')



# print(name)
# repo = g.get_user().get_repos()
# r1 = g.get_repo('immdshahid/jtest')
# print(r1.releases_url)
# for r in repo:
#     print(r.name)
# owner = "immdshahid"
# repo = "jtest"
# query_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
# params = {
#     "state": "open",
# }
# headers = {'Authorization': f'token {token}'}
# r = requests.get(query_url, headers=headers, params=params)
# pprint(r.json())

# user = input("User: ")
# __user__ = f'{user}'
# repo = input("Repository: ")
# __repo__ = f'{repo}'

# print("\nChoose the local path for your clone.")
# local = input("Local path: ")
# local_path = f'{local}'

# subprocess.Popen(['git', 'clone', "https://github.com/" + __user__ + "/" + __repo__ + ".git", local_path])

# subprocess.Popen(['https://github.com/immdshahid/jtest.git', 'log'])

# subprocess.run('log')


# repos = g.get_user.get_repo()
# con = repo.get_clones_traffic()
# print(repo.)
# for c in repos:
#  print(c.name)

# pprint(user)
