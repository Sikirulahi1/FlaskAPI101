from flask import Flask, render_templates, request

app = Flask(__name__)

@app.route("/", method = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = "Invalid username or password"
            
    return render_templates('login.html', error = error)
