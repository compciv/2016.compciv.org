from os.path import join
from operator import itemgetter

DATADIR = 'tempdata'
FPATH = join(DATADIR, 'ssa-babynames-nationwide-2014.txt')
f = open(FPATH, 'r')
mydict = {'F': [], 'M': []}
for line in f:
    name, sex, count = line.strip().split(',')
    if 'x' in name.lower():
        mydict[sex].append([name, int(count)]) # no need to re-record gender
f.close()

for sex in ['F', 'M']:
    ct = 0
    if sex == 'F':
        print("Female")
    else:
        print("Male")
    for row in sorted(mydict[sex], key=itemgetter(1), reverse=True)[0:5]:
        ct += 1
        print(str(ct) + '.', row[0].ljust(15), str(row[1]).rjust(6))


