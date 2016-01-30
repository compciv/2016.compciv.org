import os
import requests
DATA_DIR = 'tempdata'
ZIP_URL = 'http://stash.compciv.org/scrapespeare/matty.shakespeare.tar.gz'
ZIP_LOCAL_FILENAME = os.path.join(DATA_DIR, 'matty.shakespeare.tar.gz')

# Download the file
print("Downloading:", ZIP_URL)
resp = requests.get(ZIP_URL)
zdata = resp.content


# Write it to disk
print("Writing file:", ZIP_LOCAL_FILENAME)
z = open(ZIP_LOCAL_FILENAME, 'wb')
z.write(zdata)
z.close()

