# a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json"

# by Rachel King

import requests
import json

# to save the url of the dataset
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

# this function retrieves the dataset from the url above and converts it to json format
def get_all():
    response = requests.get(url)
    return response.json()

# this writes the json serialised data into a file called cso.json
if __name__ == "__main__":
    with open("cso.json", "wt") as fp:
        print(json.dumps(get_all()), file=fp)