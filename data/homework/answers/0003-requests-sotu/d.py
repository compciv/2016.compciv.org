import requests
url = 'https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-%E2%80%93-prepared-delivery-state-union-address/'
resp = requests.get(url)
print(resp.status_code)
print(len(resp.text))
