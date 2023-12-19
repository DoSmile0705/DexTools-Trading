import requests
from flask import Flask
from flask import Request

app = Flask(__name__)


@app.route('/server/login', methods=['POST', 'GET'])
def get_cred():
    dataCred = Request.data
    if (dataCred):
        
        return dataCred
    else:
        return 'sdafffffffffffffffdasfdasfasdfasfsadfasdfafdadf'
    


@app.route('/server/start', methods=['GET', 'POST'])
def home():
    return 'Hello, World!'


@app.route('/server/stop', methods=['GET', 'POST'])
def about():
    return 'About'
