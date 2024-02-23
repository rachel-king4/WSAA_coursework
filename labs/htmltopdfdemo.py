# converts a webpage to a pdf

# Author: Rachel King

import requests
import urllib.parse
from config import apikeys as cfg

targeturl = "https://en.wikipedia.org/wiki/Main_Page"

apikey = cfg["htmltopdfkey"]
apiurl = "https://api.html2pdf.app/v1/generate"

params = {'html': targeturl, 'apiKey': apikey}
parsedparams = urllib.parse.urlencode(params)

requestUrl = apiurl +"?" + parsedparams
print(requestUrl)

response = requests.get(requestUrl)

print(response.status_code)
result = response.content

with open("document.pdf", "wb") as handler:
    handler.write(result)


