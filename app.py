import json

from flask import Flask, jsonify
from flask_cors import cross_origin

app = Flask(__name__)


@app.route("/api/cars", methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def cars():
    with open('json/cars.json') as f:
        data = json.load(f)
        return jsonify(data)


app.run()
