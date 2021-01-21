import os
import requests


api_key = os.environ.get("FT_API_KEY")

payload = {
    "queryString": "banks",
    "resultContext" : {
         "aspects" :[  "title", "lifecycle", "location", "summary", "editorial" ]
    }
}
headers = {"X-Api-Key": "{}".format(api_key)}

# Content-Type=application/json

response = requests.post(
    "https://api.ft.com/content/search/v1?",
    headers=headers,
    json=payload
)

print(response.status_code)
print(response.json())