from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return f"index"

@app.route("/login")
def login():
    return f"login"

@app.route("/user/<string:username>")
def profile(username):
    return f"{username}\'s profile"


with app.test_request_context():
    print(url_for("index"))
    print(url_for("login"))
    print(url_for("login", next="/"))
    print(url_for("profile", username = "John Doe"))