import requests
from flask import Flask, jsonify, request
import jwt
import datetime

app = Flask(__name__)


@app.route('/server/login', methods=['POST', 'GET'])
def get_cred():
    dataCred = request.form
    new_email = dataCred['email']
    new_pass = dataCred['password']
    init_email = 'whaleundercover@gmail.com'
    init_pass = 'DexTools0705!'
    if (new_email == init_email and new_pass == init_pass):
        expiration = datetime.datetime.utcnow() + datetime.timedelta(days=1)

        payload = {
            'email': new_email,
            'exp': expiration
        }
        token = jwt.encode(payload, init_pass, algorithm='HS256')
        return jsonify({'token': token})

    else:
        return jsonify({'error': 'Invalid email or password'}), 401


@app.route('/server/start', methods=['GET', 'POST'])
def home():
    return 'Hello, World!'


@app.route('/server/stop', methods=['GET', 'POST'])
def about():
    return 'About'
