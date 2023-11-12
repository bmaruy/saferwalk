from flask import Flask, Blueprint
from flask_cors import CORS

from choosingRoute import routes_page

app = Flask(__name__)
CORS(app)

app.register_blueprint(routes_page, url_prefix="/route")


@app.route("/")
def home():
    return "Safer Walk Home Page"





