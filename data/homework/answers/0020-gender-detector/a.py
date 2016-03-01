import requests
from os import makedirs
from os.path import join
from shutil import unpack_archive
from glob import glob
SOURCE_URL = 'https://www.ssa.gov/oact/babynames/names.zip'
DATA_DIR = 'tempdata'
DATA_ZIP_PATH = join(DATA_DIR, 'names.zip')
# make the directory
makedirs(DATA_DIR, exist_ok=True)

print("Downloading", SOURCE_URL)
resp = requests.get(SOURCE_URL)
# save it to disk
# we use 'wb' because these are BYTES
with open(DATA_ZIP_PATH, 'wb') as f:
    # we use resp.content because it is BYTES
    f.write(resp.content)

# now let's unzip it into tempdata/
unpack_archive(DATA_ZIP_PATH, extract_dir=DATA_DIR)

# get all the filenames
babynamefilenames = glob(join(DATA_DIR, '*.txt'))
print("There are", len(babynamefilenames), 'txt files')




