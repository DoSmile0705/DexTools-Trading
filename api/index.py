import csv
from dextools_python import DextoolsAPI
from dextools_python import DextoolsAPIV2
from flask import Flask
import requests

app = Flask(__name__)


@app.route('/server/start', methods=['GET', 'POST'])
def home():
    return 'Hello, World!'


API_KEY = "9KBOGXmVLopfS4mAyYEj5G78Qklr0RGA"
NETWORK = "arbitrum"


dextools = DextoolsAPI(API_KEY)
response = dextools.get_exchange_list(NETWORK, pageSize=50)
data = response["data"]

with open("exchanges.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)

    count = 0

    for dex in data:
        if count == 0:
            header = dex.keys()
            csv_writer.writerow(header)
            count = count + 1

        csv_writer.writerow(dex.values())

    csv_file.close()

dextools = DextoolsAPIV2(API_KEY)
response = dextools.get_exchange_list(NETWORK, pageSize=50)
data = response["data"]

with open("exchanges.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)

    count = 0

    for dex in data:
        if count == 0:
            header = dex.keys()
            csv_writer.writerow(header)
            count = count + 1

        csv_writer.writerow(dex.values())

    csv_file.close()


@app.route('/server/stop', methods=['GET', 'POST'])
def about():
    return 'About'
