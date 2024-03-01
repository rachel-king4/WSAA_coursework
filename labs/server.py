from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Mamm\zmmkm\zkn"

@app.route('/blah')
def blah():
    return "this is blah"


if __name__ == "__main__":
        app.run(debug = True)