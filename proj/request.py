import requests


response = requests.get("https://geo.by", verify=False )
print(response.status_code)
