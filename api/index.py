from flask import Flask

app = Flask(__name__)


@app.route('/server/start')
def home():
    return 'Hello, World!'


@app.route('/server/stop')
def about():
    return 'About'
