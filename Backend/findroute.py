
from query_inrix import get, getToken
from flask import Blueprint
import requests

inrix_page = Blueprint('inrix_page', __name__)

@inrix_page.route("/findroutes")
def getRoutes():
    lat1 = 37.770581
    long1 = -122.442550
    lat2 = 37.766476410698715
    long2 = -122.44115572471541

    url = "https://api.iq.inrix.com/findRoute?wp_1=" + str(lat1) + "%2C"+ str(long1) +"&wp_2=" + str(lat2) + "%2C" + str(long2) + "&maxAlternates=2&format=json"


    response = get(url)

    all_routes = []
    individual_route = []


    print(len(response.get('result').get('trip').get("routes")))
    for i in range(0, len(response.get('result').get('trip').get("routes"))):
        for j in range(0, len(response.get('result').get('trip').get('routes')[i].get('summary').get('roads'))):
            individual_route.append(response.get('result').get('trip').get("routes")[i].get('summary').get('roads')[j].get('name'))
        print(individual_route)
        all_routes.append(individual_route)
        individual_route = []

    return all_routes


