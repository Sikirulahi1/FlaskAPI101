from flask import Flask, abort, redirect, url_for, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for(login))

# @app.route('/login')
# def login():
#     abort(401)
#     this_never_executed()

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'), 404

@app.errorhandler(404)
def page_not_found():
    resp = make_response(render_template('error.html'), 404)
    resp.headers['Error404'] = 'Error in this page'
    return resp