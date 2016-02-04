from os import makedirs
from os.path import join
import requests

STORAGE_DIR = 'tempdata'
BASE_FILENAME = 'stanford.json'
URL_DIR = 'http://www.compciv.org/files/datadumps/apis'
URL_PATHS = [
    'googlemaps/geocode-stanford.json',
    'mapzen/search-stanford.json'
]

# make the directory


for u in URL_PATHS:
    print("---")  # just a dividing line to make output easier to read...
    url = join(URL_DIR, u)
    print("Downloading from:", url)
    resp = requests.get(url)
    sub_dir = u.split('/')[0] # e.g. 'googlemaps' or `mapzen`
    big_dir = join(STORAGE_DIR, sub_dir) # e.g. tempdata/googlemaps
    makedirs(big_dir, exist_ok=True)
    # Finally, the full path
    fname = join(big_dir, BASE_FILENAME)
    print("Writing to:", fname)
    with open(fname, 'w') as f:
        txt = resp.text
        f.write(txt)
        print("Wrote",
              len(txt.splitlines()), 'lines and',
              len(txt), 'characters' )
