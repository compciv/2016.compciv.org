from os.path import join
import string
DATADIR = 'tempdata'
FPATH = join(DATADIR, 'ssa-babynames-nationwide-2014.txt')
mydict = {'M': {}, 'F': {}}
with open(FPATH) as f:
    for line in f:
        name, sex, babies = line.strip().split(',')
        letter = name[-1]
        if mydict[sex].get(letter):
            mydict[sex][letter] += int(babies)
        else:
            mydict[sex][letter] = int(babies)

print('letter'.ljust(8) + 'F'.rjust(8) + 'M'.rjust(8))
print("".rjust(24, '-'))
for k in string.ascii_lowercase:
    print((k).ljust(8) + str(mydict['F'][k]).rjust(8) +   str(mydict['M'][k]).rjust(8))
