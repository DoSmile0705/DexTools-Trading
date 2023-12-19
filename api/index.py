import requests
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/server/login', methods=['GET', 'POST'])
def get_cred():
    data = request.data
    print(data, type(data), "this is emaiol and apss word")


@app.route('/server/start', methods=['GET', 'POST'])
def home():
    return 'Hello, World!'


@app.route('/server/stop', methods=['GET', 'POST'])
def about():
    return 'About'
