import requests
from flask import Flask
from flask import Request


app = Flask(__name__)


@app.route('/server/login', methods=['POST', 'GET'])
def get_cred(request):
    # data = Request.get_json()
    return request.form.data['email']
    # password = data.get('password')

    # init_email = "whaleundercover@gmail.com"
    # init_pass = "DexTools0705!"

    # if (data):
    #     return 'okay'
    # else:
    #     return 'sdafffffffffffffffdasfdasfasdfasfsadfasdfafdadf'


@app.route('/server/start', methods=['GET', 'POST'])
def home():
    return 'Hello, World!'


@app.route('/server/stop', methods=['GET', 'POST'])
def about():
    return 'About'
