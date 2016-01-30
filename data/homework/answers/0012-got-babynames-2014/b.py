from os.path import join
DATADIR = 'tempdata'
FPATH = join(DATADIR, 'ssa-babynames-nationwide-2014.txt')

babies = 0
with open(FPATH) as f:
    for line in f:
        babies += int(line.split(',')[2])


print("There are", babies, "babies whose names were recorded in 2014.")
