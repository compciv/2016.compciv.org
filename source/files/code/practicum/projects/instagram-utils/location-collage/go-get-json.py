import webbrowser
from instagram_api_utils import prepare_media_search_url

ACCESS_ID = open('creds_instagram.txt').read().strip()
LATITUDE = 40.7201424
LONGITUDE = -74.0050583


url = prepare_media_search_url(ACCESS_ID, lat = LATITUDE, lng = LONGITUDE)
webbrowser.open_new(url)

