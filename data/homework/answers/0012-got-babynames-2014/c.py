from os.path import join
DATADIR = 'tempdata'
FPATH = join(DATADIR, 'ssa-babynames-nationwide-2014.txt')
dx = kx = 0
with open(FPATH) as f:
    for line in f:
        name, sex, babies = line.strip().split(',')
        if sex == 'F':
            if name == 'Daenerys':
                dx += int(babies)
            elif 'Khalees' in name or 'Khaless' in name:
                kx += int(babies)


print('Daenerys:', dx)
print('Khaleesi:', kx)
