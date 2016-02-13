# A partial answer for c.py
from os.path import join

DATADIR = 'tempdata'
FPATH = join(DATADIR, 'ssa-babynames-nationwide-2014.txt')
namesdict = {}

# The following routine creates a dictionary named
# namesdict in which every name is a key and points to the
# total number of babies (i.e. both "M" and "F")
# e.g.
# {
#     'Mackenzie': 4152
#     'Christopher': 10293
# }
#
# This is necessary because the assignment requires that
# we select the longest names from a list of names, each of
# which have been given to at least 2,000 babies
# -- M and F -- so we need to basically rebuild a list that
# is gender-agnostic and is just a list of names and numbers


with open(FPATH) as f:
    for line in f:
        name, sex, babies = line.strip().split(',')
        if namesdict.get(name):
            namesdict[name] += int(babies)
        else:
            namesdict[name] = int(babies)

# Then filter this namesdict to include only key-value pairs
# in which the value (i.e. number of babies) is at least 2,000


# Then, finally, create a sort function that sorts by
# length of name, then number of babies
