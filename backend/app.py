from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from pandas import read_csv
import os

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#running forecast
os.system("scrape.py")

#extract data
series = read_csv('new_cases.csv')
series_json = series.to_dict()

@app.get("/forecast")
@cross_origin()
def get__forecast():
    return jsonify(series_json)

