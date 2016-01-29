import requests

def prepare_media_search_url(access_token, lat, lng, distance = 1000):
    url_endpoint = 'https://api.instagram.com/v1/media/search'
    my_params = {
        'access_token': access_token,
        'lat': lat,
        'lng': lng,
        'distance': distance
    }

    req = requests.PreparedRequest()
    req.prepare_url(url_endpoint, params=my_params)
    return req.url




