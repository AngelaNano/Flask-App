import requests
BASE_URL = "http://127.0.0.1:5000"
print(requests.get(f"{BASE_URL}/api/hello").json())
print(requests.get(f"{BASE_URL}/api/data").json())
