import requests
resp = requests.get("http://example.com")
print(resp.status_code)
txt = resp.text
print(len(txt))
