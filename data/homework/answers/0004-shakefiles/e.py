import os
import glob
DATA_DIR = 'tempdata'
HAMLET_FILENAME = os.path.join(DATA_DIR, 'tragedies', 'hamlet')


linecount = 0
f = open(HAMLET_FILENAME, 'r')
for line in f:
    linecount = linecount + 1
f.close()

print(HAMLET_FILENAME, "has", linecount, "lines")
