from flask import Flask, render_template, request, url_for, redirect, Blueprint, send_from_directory, jsonify
import os
from login import login_check as lc
from register import register_on_submit as rs
import ctypes
import os.path

main = Blueprint('main', __name__)

secret_key = str(os.urandom(24))

app = Flask(__name__)
app.config['TESTING'] = False
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'deployment'
app.config['SECRET_KEY'] = secret_key

app.register_blueprint(main)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Hello, World!"

@app.route('/register', methods=['GET', 'POST'])
def register():
    request_data = request.json
    url = request_data['url']
    uid = request_data['uid']

    status = rs(uid,url)
    return status

@app.route('/login', methods=['GET', 'POST'])
def login():
    request_data = request.json
    uid = request_data['uid']
    url = request_data['url']

    status = lc(uid,url)
    return status

@app.route('/chkregister', methods=['GET', 'POST'])
def chkregister():
    request_data = request.json
    uid = request_data['uid']
    valid = os.path.exists('student/'+uid+'.png')
    status = ''
    if(valid):
        status = 'valid'
    else:
        status = 'invalid'
    return status



@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=False)
