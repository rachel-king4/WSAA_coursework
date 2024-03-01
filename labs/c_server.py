from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Mam"

@app.route('/inquery')
def inquery():
    name = request.args["name"]
    return name

@app.route("/inbody", methods=["POST"])
def inbody():
    name = request.json["name"]
    age = request.json["age"]
    return f"you are {name} and aged {age} {type(age)}"

@app.route('/user')
def get_user():
    user={
        'name': "Rachel",
        'age': 30
    }
    return jsonify(user)

if __name__ == "__main__":
    app.run(debug = True)