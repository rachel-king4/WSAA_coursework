# gets info from private repository on github
# and outputs the results to a file

# Author: Rachel King

import requests
import json
from config import apikeys as cfg

filename = "repos_private.json"

url = "https://api.github.com/repos/rachel-king4/aprivateone"

apikey = cfg["privaterepokey"]
response = requests.get(url, auth = ("token", apikey))
#response = requests.get(url)

print(response.status_code)

with open(filename, "w") as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)