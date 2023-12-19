import requests
from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/server/login', methods=['POST', 'GET'])
def get_cred():
    dataCred = request.form
    new_email = dataCred['email']
    new_pass = dataCred['password']
    init_email = 'whaleundercover@gmail.com'
    init_pass = 'DexTools0705!'
    if (new_email == init_email and new_pass == init_pass):
        return 'ok'
    else:
        return 'Not'         

@app.route('/server/start', methods=['GET', 'POST'])
def home():
    return 'Hello, World!'


@app.route('/server/stop', methods=['GET', 'POST'])
def about():
    return 'About'
