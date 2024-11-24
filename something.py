import requests

url = "http://indianrailapi.com/api/v2/TrainSchedule/apikey/41758ae2c7c3e4ae790c76cf1ac2dffd/TrainNumber/15007"
headers = {
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

# Check response
if response.headers.get('Content-Type') == 'application/json':
    print(response.json())  # JSON response
else:
    print(response.text)  # Fallback for non-JSON response
