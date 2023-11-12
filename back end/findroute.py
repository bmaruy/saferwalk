
from query_inrix import get, getToken


def getRoutes(lat1, long1, lat2, long2):

    url = "https://api.iq.inrix.com/findRoute?wp_1=" + str(lat1) + "%2C"+ str(long1) +"&wp_2=" + str(lat2) + "%2C" + str(long2) + "&maxAlternates=2&format=json"


    response = get(url)

    all_routes = []
    individual_route = []


    #print(len(response.get('result').get('trip').get("routes")))
    for i in range(0, len(response.get('result').get('trip').get("routes"))):
        for j in range(0, len(response.get('result').get('trip').get('routes')[i].get('summary').get('roads'))):
            individual_route.append(response.get('result').get('trip').get("routes")[i].get('summary').get('roads')[j].get('name'))
        print(individual_route)
        all_routes.append(individual_route)
        individual_route = []
    #print(all_routes)
    return all_routes

def getDistances(lat1, long1, lat2, long2):

    url = "https://api.iq.inrix.com/findRoute?wp_1=" + str(lat1) + "%2C" + str(long1) +"&wp_2=" + str(lat2) + "%2C" + str(long2) + "&maxAlternates=2&format=json"

    response = get(url)
    total_distances = []

    for i in range(0, len(response.get('result').get('trip').get("routes"))):
        total_distances.append(response.get('result').get('trip').get('routes')[i].get('totalDistance'))

    return total_distances

def getCornerCoords(i, lat1, long1, lat2, long2):
    url = "https://api.iq.inrix.com/findRoute?wp_1=" + str(lat1) + "%2C" + str(long1) + "&wp_2=" + str(
        lat2) + "%2C" + str(long2) + "&maxAlternates=2&format=json"

    response = get(url)

    coords = []
    for j in range(len(response.get('result').get('trip').get("routes")[i].get("boundingBox"))):
        corn = "corner" + str(j + 1)
        coords.append(response.get('result').get('trip').get('routes')[i].get('boundingBox').get(corn).get('coordinates'))

    return coords