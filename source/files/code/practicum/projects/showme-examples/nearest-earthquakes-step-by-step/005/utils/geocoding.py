import requests
import json


def read_mapzen_credentials():
    creds_filename = "creds_mapzen.txt"
    keytxt = open(creds_filename).read().strip() # e.g. "search-blahblah"
    return keytxt



def fetch_mapzen_response(location):
    """
    `location` is a string that will be passed onto Mapzen API for geocoding

    returns a text string containing JSON-formatted data from Mapzen
    """

    # ignore the location string for now
    SAMPLE_DATA_URL = 'http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json'
    resp = requests.get(SAMPLE_DATA_URL)
    return resp.text

def parse_mapzen_response(txt):
    """
    `txt` is a string containing JSON-formatted text from Mapzen's API

    returns a dictionary containing the useful key/values from the most
       relevant result.
    """
    gdict = {} # just initialize a dict for now, with status of None
    data = json.loads(txt)
    if data['features']: # it has at least one feature...
        gdict['status'] = 'OK'
        feature = data['features'][0] # pick out the first one
        props = feature['properties']  # just for easier reference
        gdict['confidence'] = props['confidence']
        gdict['label'] = props['label']

        # now get the coordinates
        coords = feature['geometry']['coordinates']
        gdict['longitude'] = coords[0]
        gdict['latitude'] = coords[1]
    else:
        gdict['status'] = None
    return gdict

def geocode(location):
    """
    Attempt to geocode a location string using Mapzen Search API

    What it expects:
    ----------------
    It expects `location` is a string, representing some kind of human-readable
      geographical location, e.g. "Stanford, CA"

    It also expects the variable `CREDS_FILE` to point to an existing file
    that contains a valid Mapzen Search key.

    What it does:
    -------------
    It opens and reads the file at CREDS_FILE to get the API key.

    It calls the Mapzen Search API via a HTTP request, using the API key,
    and the user-provided `location` string as the `text` parameter.

    It deserializes the Mapzen Search response into a dictionary, using
    the JSON library.

    It then creates a dictionary

    What it returns:
    ----------------
    A dictionary containing these key-value pairs:

    - query_text: the `location` string provided by the user
    - label: The string label that Mapzen provides in describing the found location
    - confidence: A float representing the confidence value that Mapzen has in its result.
    - latitude: a float representing the latitude coordinate
    - longitude: a float representing the longitude coordinate
    """
    rawtext = fetch_mapzen_response(location)
    mydict = parse_mapzen_response(rawtext)
    # add the location string to mydict
    mydict['query_string'] = location
    # return the diccionary
    return mydict
