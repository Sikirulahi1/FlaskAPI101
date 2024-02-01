from flask import Flask, request

app = Flask(__name__)

@app.route("/login", method = ["GET", 'POST'])
def login():
    if request.method == "POST":
        return do_the_login()
    else:
        return show_the_login_form()
    
# Or it can be done this way

@app.get("/login")
def login_post():
    return show_the_login_form()

@app.post_get("/login")
def login():
    return do_the_login()