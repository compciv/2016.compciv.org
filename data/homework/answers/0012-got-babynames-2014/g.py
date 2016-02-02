from os.path import join
import string
DATADIR = 'tempdata'
FPATH = join(DATADIR, 'ssa-babynames-nationwide-2014.txt')
mydict = {'M': {}, 'F': {}}
with open(FPATH) as f:
    for line in f:
        name, sex, babies = line.strip().split(',')
        letter = name[-1]
        # THIS IS JUST THE PARTIAL ANSWER. WELL JUST ONE PARTIAL
        # ANSWER ANYWAY...
