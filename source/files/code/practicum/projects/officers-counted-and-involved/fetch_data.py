from os import makedirs
from os.path import join, basename
from shutil import unpack_archive
import requests
DATA_DIR = 'tempdata'
URL = 'https://interactive.guim.co.uk/2015/the-counted/thecounted-data.zip'
ZIP_FILE_NAME = join(DATA_DIR, basename(URL))

# make the directory
makedirs(DATA_DIR, exist_ok=True)
print("Downloading", URL)
zcontent = requests.get(URL).content
# write to disk
print("Saving to", ZIP_FILE_NAME)
with open(ZIP_FILE_NAME, "wb") as zf:
    zf.write(zcontent)
print("Unzipping", ZIP_FILE_NAME, "to", DATA_DIR)
unpack_archive(ZIP_FILE_NAME, extract_dir = DATA_DIR)
