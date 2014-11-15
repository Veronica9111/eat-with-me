#!/usr/bin/env python

from flask import Flask
from flask import render_template, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/place")
def place():
    return render_template('place.html')

@app.route("/places", methods=["GET"])
def get_places():
    data = [{"name": "Restaurant 1", "location": "blablabla"}]
    return jsonify({'data': data})

if __name__ == "__main__":
    app.run(debug=True)
