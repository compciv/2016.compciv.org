from os import makedirs
from os.path import basename, join
import requests
DATADIR = 'tempdata'
makedirs(DATADIR, exist_ok=True)
URL = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
FPATH = join(DATADIR, basename(URL))

data = requests.get(URL).text

# Note: this is the "cool" way to open and close files
# at the end of the block, `f` will automatically be closed
with open(FPATH, 'w') as f:
    f.write(data)

# Alternatively:
# f = open(FPATH, 'w')
# f.write(data)
# f.close()

print("There are", len(data.splitlines()), 'lines in', FPATH)
