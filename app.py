"""app.py
K. Outcalt | A. Goyal | M. Cruz
RESTful API for postal address project
3.9.22
"""
from flask import Flask, request, jsonify
# request is the request object from the client
# jsonify wraps texts/dictionaries in a json

app = Flask(__name__)

# getting a country-specific postal address format
@app.route("/country", methods=['GET'])
def get_country_format():
    return jsonify("Country successfully received")

# getting a list of potential addresses for a submitted address
@app.route("/submit", methods=['GET'])
def submit_address():
    return jsonify("Address successfully received")