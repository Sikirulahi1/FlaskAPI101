from flask import Flask
from markupsafe import escape

application = Flask(__name__)

@application.route("/<name>")
def say_hello(name):
    return f"<p>Hello {escape(name)}"

if __name__ == "__main__":
    application.run(debug=True)