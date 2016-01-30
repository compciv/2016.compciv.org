import requests
url = 'https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-%E2%80%93-prepared-delivery-state-union-address'
resp = requests.get(url)

# Being super verbose here...
txt = resp.text
a = txt.count('Applause')
print(a)
b = txt.lower().count('applause')
print(b)
c = txt.count('<p>')
print(c)


# Could also just be this:
#
# print(resp.text.count('Applause'))
# print(resp.text.lower().count('applause'))
# print(resp.text.count('<p>'))
#
# but that looks a bit unwieldy to the common eye...
