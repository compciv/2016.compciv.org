from os.path import join
from collections import defaultdict

DATADIR = 'tempdata'
FPATH = join(DATADIR, 'ssa-babynames-nationwide-2014.txt')
names = defaultdict(int)

with open(FPATH) as f:
    for line in f:
        name, sex, babies = line.strip().split(',')
        names[name] += int(babies)


bignames = {}
for k, v in names.items():
    if v >= 2000:
        bignames[k] = v


def foo(x):
    return (len(x[0]), x[1])


for i, n in enumerate(sorted(list(bignames.items()), key = foo, reverse=True)[0:10]):
    name, count = n
    print(name.ljust(15), str(count).rjust(8))


