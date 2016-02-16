def feedme(lng, lat):
    """
    Filter a dataset based on distance from a geocoordinate pair and
     return the 5 nearest records

    What it expects:
    ----------------
    lng (number) - a longitude coordinate
    lat (number) - a latitude coordinate

    What it does:
    -------------
    Reads from the data at WRANGLED_FILENAME
    and sorts the data in order of proximity to the lng, lat coordinates

    What it returns:
    ----------------
    A list of 5 dictionaries, each dictionary representing one of the
      5 closest data records
    """

    return ['something', 'something', 'something', 'something' ,'something']



def haversine_foo(a, b):
    """
    `a` and `b` are tuples with two float numbers each, i.e.
    representing lng/lat pairs:
    (99,100)  (-42, 85)

    The geo distance between the two points is returned in kilometers
    """
    from math import radians, cos, sin, asin, sqrt

    lng_a = radians(a[0])
    lng_b = radians(b[0])
    lat_a = radians(a[0])
    lat_b = radians(b[0])
    # haversine formula
    dlng = lng_b - lng_a
    dlat = lat_b - lat_a
    whatevs = sin(dlat /2 ) ** 2 + cos(lat_a) * cos(lat_b) * sin(dlng / 2) ** 2
    c = 2 * asin(sqrt(whatevs))
    r = 6371 # Radius of earth in kilometers.
    # return the final calculation
    return c * r
