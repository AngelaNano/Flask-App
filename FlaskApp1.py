import requests
BASE_URL = "http://127.0.0.1:5000"
print(requests.get(f"{BASE_URL}/hello").json())
print(requests.get(f"{BASE_URL}/data").json())
