import requests
from flask import Flask
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


@app.route('/server/login', methods=['POST', 'GET'])
def get_cred():
    # dataCred = request.data
    # if (dataCred):
    #     return 'ok'
    # else:
        return 'sdafffffffffffffffdasfdasfasdfasfsadfasdfafdadf'


@app.route('/server/start', methods=['GET', 'POST'])
def home():
    return 'Hello, World!'


@app.route('/server/stop', methods=['GET', 'POST'])
def about():
    return 'About'
