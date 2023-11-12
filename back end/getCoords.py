import requests


def getCoords():
    url = "https://localhost:5000"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.json()

    coords = []

    coords.append((res[0], res[1]))
    coords.append((res[2], res[3]))

    return coords