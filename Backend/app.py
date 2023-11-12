from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

from findroute import getRoutes, inrix_page

app = Flask(__name__)
CORS(app)

app.register_blueprint(inrix_page, url_prefix="/inrix")


@app.route("/")
def home():
    return "Safer Walk Home Page"





