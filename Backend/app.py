from flask import Flask
from flask_cors import CORS

from findroute import getRoutes, inrix_page
from query_geonames import geonames_page

app = Flask(__name__)
CORS(app)

app.register_blueprint(inrix_page, url_prefix="/inrix")
app.register_blueprint(geonames_page, url_prefix="/geonames")


@app.route("/")
def home():
    return "Safer Walk Home Page"





