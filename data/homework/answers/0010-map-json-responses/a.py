from os import makedirs
from os.path import join
import requests

STORAGE_DIR = 'tempdata'
BASE_FILENAME = 'stanford.json'
URL_DIR = 'http://www.compciv.org/files/datadumps/apis'

# I arrange things this way because I see in the
# given URLs that the first part of the URL
# is the same...not only that, I *know*
# that the subdirectories we want to make can be found
# in partial URL path itself
PARTIAL_URL_PATHS = [
    'googlemaps/geocode-stanford.json',
    'mapzen/search-stanford.json'
]



for upath in PARTIAL_URL_PATHS:
    print("---")  # just a dividing line to make output easier to read...
    url = join(URL_DIR, upath)
    print("Downloading from:", url)
    resp = requests.get(url)
    # the subdirectories, e.g. tempdata/mapzen
    # can be extracted from each partial URL_PATH
    # e.g. mapzen/search-stanford.json
    sub_dir = upath.split('/')[0]
    big_dir = join(STORAGE_DIR, sub_dir) # e.g. tempdata/googlemaps
    # create the directory, e.g. tempdata/googlemaps
    makedirs(big_dir, exist_ok=True)
    # Finally, the full path
    # e.g. tempdata/googlemaps.stanford.json
    fname = join(big_dir, BASE_FILENAME)
    print("Writing to:", fname)
    f = open(fname, 'w')
    txt = resp.text
    f.write(txt)
    print("Wrote",
          len(txt.splitlines()), 'lines and',
          len(txt), 'characters' )
    f.close()
