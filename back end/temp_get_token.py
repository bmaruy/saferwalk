import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def getToken():
    url = "https://api.iq.inrix.com/auth/v1/appToken?appId=66rxplb0t6&hashToken=NjZyeHBsYjB0Nnx5eDMzQlgwTmU3NkQ2S09LblV2Z0UxWkppZXJ6R2k0eTdIb3pIYlpW"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    res = response.json()
    app_token = res['result']['token']

    return app_token

if __name__ == '__main__':
    app.run(debug=True)
