import requests

base_url = "http://localhost:3000/api/v1/analysis/"
params = {
    "uri": "http://jeroen.github.io/images/testocr.png"
}

# Sending the GET request
response = requests.get(base_url, json=params)

print(response)