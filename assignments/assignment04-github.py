# a program that reads a file from a repository
# and replaces all instances of "Andrew" with "Rachel"
# and commit the changes and push file to repository

# by Rachel King

import requests
from github import Github
from config import apikeys as cfg

apikey = cfg["privaterepokey"]
g = Github(apikey)

repo = g.get_repo("rachel-king4/aprivateone")

file_info = repo.get_contents("test.txt")
url_of_file = file_info.download_url


response = requests.get(url_of_file)
content_of_file = response.text
#print (contentOfFile)

new_contents = content_of_file.replace("Andrew", "Rachel")
#print(new_contents)

github_response=repo.update_file(file_info.path,"updated by prog",
new_contents,file_info.sha)
print (github_response)