from os.path import join
from operator import itemgetter

DATADIR = 'tempdata'
FPATH = join(DATADIR, 'ssa-babynames-nationwide-2014.txt')
records = []
with open(FPATH) as f:
    for line in f:
        name, sex, babies = line.strip().split(',')
        row = [name, sex, int(babies)]
        records.append(row)


# create a new list, sorted by the third element of each row
ordered_records = sorted(records, key=itemgetter(2), reverse=True)


# create a sub list of the newlist
top_10_records = ordered_records[0:10]

for i, row in enumerate(top_10_records):
    row[-1] = str(row[-1])
    print(str(i + 1) + '.',  ','.join(row))
