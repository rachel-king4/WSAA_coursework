import requests
import json
url = "http://andrewbeatty1.pythonanywhere.com/books"

def readbooks():
    response = requests.get(url)
    # we could do checking for correct response code here
    return response.json()


def getallbooks():
    response = requests.get(url)
    return response.json()


def getbookbyid(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()


def createbook(book):
    book = {
        "Author": "test",
        "Title": "title",
        "Price": 123
    }
    response = requests.post(url, json=book)
    return response.json()


def updatebook(id, bookdiff):
    updateurl = url + "/" + str(id)
    response = requests.put(updateurl, json=bookdiff)
    return response


def deletebook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()


if __name__ == "__main__":
    #print(getallbooks())
    #print(getbookbyid(1))
    #print(deletebook(77))
    print(createbook({}))