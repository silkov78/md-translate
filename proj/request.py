import requests


response = requests.get("https://geo.by")
print(response.status_code)
