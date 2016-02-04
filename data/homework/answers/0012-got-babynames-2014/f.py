from os.path import join
import string
DATADIR = 'tempdata'
FPATH = join(DATADIR, 'ssa-babynames-nationwide-2014.txt')
mydict = {}
with open(FPATH) as f:
    for line in f:
        name, sex, babies = line.strip().split(',')
        last_letter = name[-1]
        if mydict.get(last_letter):
            mydict[last_letter] += int(babies)
        else:
            mydict[last_letter] = int(babies)

for k in string.ascii_lowercase:
    val = mydict[k]
    print(k + ':', val)
