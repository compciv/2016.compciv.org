from os.path import join
from collections import defaultdict

DATADIR = 'tempdata'
FPATH = join(DATADIR, 'ssa-babynames-nationwide-2014.txt')
namesdict = defaultdict(int)
with open(FPATH) as f:
    for line in f:
        name, sex, babies = line.strip().split(',')
        namesdict[name] += int(babies)

def foo(x):
    return x[1]

sortednames = sorted(list(namesdict.items()), key = foo, reverse=True)
total_babies = 0
for a, b in sortednames:
    total_babies += b


ranges = [(0, 10), (10, 100), (100, 1000),
            (1000, 10000), (10000, len(names))]

for r in ranges:
    x, y = r
    z = 0
    for a, b in sortednames[x:y]:
        z += b
    print("Names", x + 1, "to", str(y) + ':', round(100 * z / total_babies, 1) )
