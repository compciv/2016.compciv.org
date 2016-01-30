from os import makedirs
from os.path import basename, join
import requests
DATADIR = 'tempdata'
makedirs(DATADIR, exist_ok=True)
URL = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
FPATH = join(DATADIR, basename(URL))

data = requests.get(URL).text
with open(FPATH, 'w') as f:
    f.write(data)


print("There are", len(data.splitlines()), 'lines in', FPATH)
