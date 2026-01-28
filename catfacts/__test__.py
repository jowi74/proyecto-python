import requests

URL = "https://catfact.ninja/fact"

response = requests.get(URL)
data = response.json()

print(data)
