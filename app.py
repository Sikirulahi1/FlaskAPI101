from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello():
    return "Say hello"

@app.route("/about")
def about():
    return "About our company"

@app.route("/help")
def help():
    return "Help us"


# Variable nd variable types
@app.route("/user/<username>")
def show_username(username):
    # Show the user profile of the user
    return f" Your username is {escape(username)}"

@app.route("/id/<int:profile_id>")
def show_id(profile_id):
    # Show that the given id is an integer
    return f" {profile_id} is your profile_id"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


if __name__ == "__main__":
    app.run(debug=True)