import requests


def getNearestIntersection(lat1, long1):
    username = "bmaru"

    url = "http://api.geonames.org/findNearestIntersectionJSON?lat=" + str(lat1) + "&lng=" + str(long1) + "&username=" + username
    response = requests.get(url)
    return response.json()






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



