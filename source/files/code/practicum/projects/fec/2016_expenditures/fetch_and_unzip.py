from os import makedirs
from os.path import join
from urllib.request import urlretrieve
from shutil import unpack_archive
DATA_DIR = 'tempdata'
# each FTP file path looks like this
# ftp://ftp.fec.gov/FEC/2016/cm16.zip
FTP_DIR = 'ftp://ftp.fec.gov/FEC/2016/'
DATA_STUBNAMES = ['cm', 'cn', 'ccl', 'oppexp']
YEAR_NAME = '16'

# Make the directory, e.g. tempdata/16
YEAR_DATA_DIR = join(DATA_DIR, YEAR_NAME)
makedirs(YEAR_DATA_DIR, exist_ok=True)

for _n in DATA_STUBNAMES:
    _fn = _n + YEAR_NAME + '.zip' # e.g. cn16.zip
    zurl = FTP_DIR + _fn # e.g. ftp://ftp.fec.gov/FEC/2016/cn16.zip
    fname = join(YEAR_DATA_DIR, _fn) # e.g. tempdata/16/cn16.zip
    print("Downloading:", zurl, "to:", fname)
    urlretrieve(zurl, filename = fname)
    unpack_archive(fname, extract_dir=YEAR_DATA_DIR)

