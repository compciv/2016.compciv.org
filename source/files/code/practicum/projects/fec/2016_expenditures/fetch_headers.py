from os import makedirs
from os.path import join
import requests
DATA_DIR = 'tempdata'
YEAR_NAME = '16'
YEAR_DATA_DIR = join(DATA_DIR, YEAR_NAME)
# Full URL is something like:
# http://www.fec.gov/finance/disclosure/metadata/cm_header_file.csv
DATA_STUBNAMES = ['cm', 'cn', 'ccl', 'oppexp']
HTTP_META_DIR = 'http://www.fec.gov/finance/disclosure/metadata/'

makedirs(YEAR_DATA_DIR, exist_ok=True) # we don't know that this exists yet...
for _n in DATA_STUBNAMES:
    _fn = _n + '_header_file.csv'
    url = HTTP_META_DIR + _fn
    fname = join(YEAR_DATA_DIR, _fn)
    print("Downloading:", url, "saving to:", fname)
    resp = requests.get(url)
    with open(fname, 'w') as f:
        f.write(resp.text)




