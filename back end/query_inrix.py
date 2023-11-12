import requests

def getToken():
    url = "https://api.iq.inrix.com/auth/v1/appToken?appId=66rxplb0t6&hashToken=NjZyeHBsYjB0Nnx5eDMzQlgwTmU3NkQ2S09LblV2Z0UxWkppZXJ6R2k0eTdIb3pIYlpW"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    res = response.json()
    app_token = res['result']['token']

    return app_token

def get(url):
    app_token = getToken()
    header = {"Authorization": f"Bearer {app_token}"}
    result = requests.get(url, headers=header)
    return result.json()




