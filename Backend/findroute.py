import requests
from query_inrix import get, getToken
from flask import Blueprint, jsonify, request, Response
import requests

inrix_page = Blueprint('inrix_page', __name__)

@inrix_page.route("/findroutes")
def getRoutes():
    lat1 = 37.775719
    long1 = -122.483438
    lat2 = 37.757400
    long2 = -122.481549

    url = "https://api.iq.inrix.com/findRoute"

    payload = {}
    params = {
        "format": "json",
        "wp_1": f'{lat1},{long1}',
        "wp_2": f'{lat2},{long2}',
        "maxAlternatives": 2,
        "criteria": "H",
        "routeType": 1
    }

    response = get(url, params)

    #find_routes = response.json()

    all_routes = []
    individual_route = []



    for i in range(0, len(response.get('result').get('trip').get("routes"))):
        for j in range(0, len(response.get('result').get('trip').get('routes')[i].get('summary').get('roads'))):
            individual_route.append(response.get('result').get('trip').get("routes")[i].get('summary').get('roads')[j].get('name'))
        all_routes.append(individual_route)
        individual_route = []
        #print(response.get('result').get('trip').get("routes")[i].get('text'))
    return all_routes
        #response.get('result').get('trip').get("routes")[1].get('summary').get('text')






'''



    params = {
        "format": "json",
        "wp_1": f'{lat1},{long1}',
        "wp_2": f'{lat2},{long2}',
        "maxAlternates": 2
    }
    url = "https://api.iq.inrix.com/v1/findRoute"

    #schedule.every().hour.do(getToken())

    #while True:
     #   schedule.run_pending()
      #  time.sleep(1)

    find_routes = get("https://api.iq.inrix.com/findRoute", params)

    payload = {}

    res = get(url, params)
'''



