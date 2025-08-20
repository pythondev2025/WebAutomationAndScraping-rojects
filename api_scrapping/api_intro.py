import requests
import json


url = "https://remoteok.com/api/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0"

request_header = {
    "User-Agent": user_agent,
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://remoteok.com",
    "Accept-Encoding": "gzip, deflate, br",
}

session = requests.Session()
session.headers.update(request_header)
response = session.get(url=url, timeout=10)

print(response.text)
print(response.status_code)

