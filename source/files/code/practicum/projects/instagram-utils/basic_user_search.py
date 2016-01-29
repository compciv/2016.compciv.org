import requests
ENDPOINT_URL = 'https://api.instagram.com/v1/users/search'
USERNAME = 'stanford'
CREDS_FILE_NAME = 'creds_instagram.txt'
my_params = {'q': USERNAME}
# get our token
with open(CREDS_FILE_NAME, 'r') as f:
    my_params['access_token'] = f.read().strip()


resp = requests.get(ENDPOINT_URL, params=my_params)
for d in resp.json()['data']:
    print("\t".join([d['username'], d['id'], d['full_name']]))


