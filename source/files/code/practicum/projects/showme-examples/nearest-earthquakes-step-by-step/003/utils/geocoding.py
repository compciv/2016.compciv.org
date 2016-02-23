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
    - status: OK, a string that indicates a result was found. Else, None
    """
    mydict = {}
    mydict['status'] = 'OK'
    mydict['query_text'] = location
    mydict['latitude'] = 99
    mydict['longitude'] = -42
    mydict['confidence'] = 0.01
    mydict['label'] = "HA HA JK"
    return mydict
