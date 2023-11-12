import requests
import schedule
import time


'''
def get_auth_token(self):
    app_id = "66rxplb0t6"
    hash_token = "NjZyeHBsYjB0Nnx5eDMzQlgwTmU3NkQ2S09LblV2Z0UxWkppZXJ6R2k0eTdIb3pIYlpW"
    url = "https://api.iq.inrix.com/auth/v1/appToken?appId=66rxplb0t6&hashToken=NjZyeHBsYjB0Nnx5eDMzQlgwTmU3NkQ2S09LblV2Z0UxWkppZXJ6R2k0eTdIb3pIYlpW"

    payload = {}
    headers = {}
    
    response = requests.request("GET", url, headers=headers, data=payload)

    res = response.json()
    self.app_token = res["result"]["token"]

    return self.app_token
'''





def getToken():
    url = "https://api.iq.inrix.com/auth/v1/appToken?appId=66rxplb0t6&hashToken=NjZyeHBsYjB0Nnx5eDMzQlgwTmU3NkQ2S09LblV2Z0UxWkppZXJ6R2k0eTdIb3pIYlpW"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    res = response.json()
    app_token = res['result']['token']

    return app_token

def get(url, params):
    app_token = getToken()
    #app_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjY2cnhwbGIwdDYiLCJ0b2tlbiI6eyJpdiI6IjVhZTA0OGZlYTVkMjU3ZmQ0MTdjMTIyYjNiZGU0MmRkIiwiY29udGVudCI6IjFhYzExZjQ5MWY1MzM4YjA5NDlhNGU3MWI2ZGMxZmYzZjY1ZjI3ZDU5MGVmNjkzMTg5MDhmOGNkODk4MWFjMzE2YzE2ZGVhZTdkNWI3NDkxZTJlMzk4ZjFmNjYyYTUzMjMyMDMzZjYzNzAwODllY2U5MjJkZDAwMTA0ZjhjNGI0ZGEzYzc1YTYyMTYzNzUyYTk1MzlhZjZlNmVmOThmNTJhOTVkZTZhZDM5ZTdmM2ZiYjUzZDA0YmZiODVkM2U4OGQ5OTRiY2I2ODMwOTIzNzZhN2RkM2RiNWVjYTAzZDdhOWM0ZDBmOTVlMzA3OTFmZmI3NjU0OGJlZWNiNzI2MjY1MmJiMDViMzg0YWNmMDM4NjAyOGJhZDU0ZjQ1ZjVlZmIyZmMyN2UwYTU5ZmFjODY3MTU2ZTNhNDQ0OWI5NDkyMDk4NzUzMzYzYmEzZmVkMGRkNTdlYWE2ZGZiNjAyMjk0NDU4MDEzNzNlOTY1MWI4ZDQ0MjNiZDAzZWNmYTdlMmFhYmI4NzJkMDg2NWRmODhiMjJmMjRmM2ViMDY2OTIxNWM1ZjE3OTBkYjJjODBlMTEyMGY1MDY2MWY4N2RjMGUzZGM1NGViMjlmOTMwMjhjNDA1MjZjNGJjNmQyNWRmNDlmMjEyZjBkNGYyMjMxZGY5NTk5MzdmY2EzNGRlNzQxY2I2MjU5MGNlODQwYTM2M2ZkMDA0Y2RlYzAwMzk3Yjg0ZTdiNmQ5ZmY2ZDI1NzFlZTQyNWU2NDE1NWI2ZWFhMjFjY2Q3ZmUyOGY3ZDYwYzRhNTM5ZmQ5MmY3ZTA0MDZhMDhkMzJlNjZmNDM0NzlhMGJiNWU2YzUzMDMxYzdiYTI3MDhjYTAyMzk0MjVkZjgyZTgwM2E2In0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiI1YWUwNDhmZWE1ZDI1N2ZkNDE3YzEyMmIzYmRlNDJkZCIsImNvbnRlbnQiOiIxYmQ0Mzg2MDA0NDU3MWIwOWVhNDYxNGQ4N2M3MGU4ZmY0MDcwMGU5YTBlNjU4NDVkMzMzZTQ5ZWYwZGI5ZjU5NTAxYWZjZjUzYjZkMjBiMGZjZTliM2NmIn0sImp0aSI6IjliYzJlYTIzLTU3MTctNDBjNi1iZjRjLTM3MmJkZTQ4OTNkNyIsImlhdCI6MTY5OTc2ODYyOCwiZXhwIjoxNjk5NzcyMjI4fQ._P6uLd2qsj9Lks1pmF5wC19umpTNj3N_cDjRAS904pI"
    header = {"Authorization": f"Bearer {app_token}"}
    result = requests.get(url, headers=header, params=params)
    return result.json()




