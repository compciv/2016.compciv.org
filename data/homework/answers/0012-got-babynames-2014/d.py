from os.path import join
DATADIR = 'tempdata'
FPATH = join(DATADIR, 'ssa-babynames-nationwide-2014.txt')

mx = fx = 0

with open(FPATH) as f:
    print("Top baby girl names")
    for line in f:
        name, sex, babies = line.strip().split(',')
        babies = line.split(',')[2].strip()
        if fx < 5:
            fx += 1
            print(str(fx) + '.', name,  babies)
        else:
            # done with girls
            print("")
            break

    print("Top baby boy names")
    for line in f:
        name, sex, babies = line.strip().split(',')
        if mx < 5 and sex == 'M':
            mx += 1
            print(str(mx) + '.', name,  babies)

