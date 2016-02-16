def publish(location):
    """
    What it expects:
    ----------------
    `location` is a string, representing some kind of human-readable
      geographical location

    What it does:
    -------------
    Geocodes the location string.
    Then uses filtrate() to get the most relevant earthquakes
    Then produces a webpage with the data
    Then uses webbrowser.open() to send the viewer directly to that page

    What it returns:
    ----------------
    Nothing
    """


# super lazy!
def google_static_map_url(marker):
    """
    marker is a string, e.g. "Ohio" or "34,-78.9"
    """
    basicurl = 'https://maps.googleapis.com/maps/api/staticmap?size=600x400&zoom=7'
    return basicurl + "&markers=" + marker




def friendly_timestamp(uglytimestamp):
    """
    uglytimestamp is something like:
        "2016-01-19T19:04:42.830Z"

    Returns:
        'Tuesday, January 16, 2016, 7:04 PM'
    """
    from dateutil import parser
    dateobj = parser.parse(uglytimestamp)
    return dateobj.strftime("%A, %B %y, %Y, %-l:%M %p")
