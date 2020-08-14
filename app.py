from flask import Flask, jsonify
import json


app = Flask(__name__)


@app.route("/api/meteo")
def meteo():
    with open('json/cars.json') as f:
        data = json.load(f)
        return jsonify(data)


app.run()
