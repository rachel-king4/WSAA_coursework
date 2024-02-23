import requests
from github import Github
from config import apikeys as cfg

apikey = cfg["privaterepokey"]
# use your own key
g = Github(apikey)

repo = g.get_repo("rachel-king4/aprivateone")
#print(repo.clone_url)

#for repo in g.get_user().get_repos():
# print(repo.name)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print(urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)

newContents = "Andrew hurried down the bustling city street, his mind consumed with thoughts of the important meeting ahead. As he rounded the corner, he bumped into an old friend he hadn't seen in years. Andrew, is that really you? she exclaimed, causing a smile to spread across his face. The unexpected reunion brought a sense of warmth to his heart, reminding him of the connections that truly matter in life. \n"
#print(newContents)

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
newContents,fileInfo.sha)
print (gitHubResponse)


