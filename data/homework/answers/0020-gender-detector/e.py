from os.path import join, basename
# we're only dealing with one file, i.e. yob2014.txt
# but it's worth storing its "year" value in a variable just to abstract things
YEAR = 2014
DATA_DIR = 'tempdata'
thefilename = join(DATA_DIR, 'yob' + str(YEAR) + '.txt')

names_dict = {}
thefile =  open(thefilename, 'r')
for line in thefile:
    name, gender, count = line.split(',')
    # Every name can show up twice for a year, as M or F
    # but some names only show up for either M or F
    # that means we need to initialize a new value
    # for a given name in names_dict if it doesn't already exist
    if not names_dict.get(name):
        # i.e. names_dict does not yet have `name` as a valid key
        # so we make it a valid key by initializing it and pointing it to
        # a dictionary that we can add values to
        names_dict[name] = {'M': 0, 'F': 0}

    # Now that names_dict[name] is itself a dictionary, {'M': 0, 'F': 0}
    # we can safely add the `count` variable to it
    #  e.g. names_dict['Jennifer']['F'] = int("24222")
    names_dict[name][gender] += int(count)
# at this point, when the for loop is done
# we're done reading from the file, so we can close it
thefile.close()

# names_dict now contains a dict of dicts:
# {
#    'Jennifer': {'F': 24222, 'M': 32},
#    'Amanda':   {'F': 10000, 'M': 0 },
#    'John':     {'F': 12,    'M': 12000}
# }


############################################################
# Now it's time to print things...
# The year 20YY has XXXXX unique names for ZZZZ total babies

# which means we need to get the total number of baby names,
# which is simply a len() call on the keys of names_dict
total_namecount = len(names_dict.keys())

# and then we need to get the total baby count...here's one straightforward
# way to do it:
total_babycount = 0
for v in names_dict.values():
    totes = v['M'] + v['F'] # count up males and females
    # and add it to the total_babycount
    total_babycount += totes

# or, you could've done this:
# ...sum(v['F'] + v['M'] for v in names_dict.values())

print("Total:", total_namecount, 'unique names for', total_babycount, 'babies')

# now we do the same thing, except for just boys and their names
ncount = 0
bcount = 0
for v in names_dict.values():
    # don't count it as a boy name if no babies were actually given the name
    if v['M'] > 0:
        bcount += v['M']
        ncount += 1
print("    M:", ncount, "unique names for", bcount, "babies")


# now we do the same thing, except for just girls and their names
ncount = 0
bcount = 0
for v in names_dict.values():
    # don't count it as a girl name if no babies were actually given the name
    if v['F'] > 0:
        bcount += v['F']
        ncount += 1
print("    F:", ncount, "unique names for", bcount, "babies")


# or if you wanted to be thrifty and not repeat yourself, do a for loop:
# for gender in ['M', 'F']:
#     ncount = 0
#     bcount = 0
#     for v in names_dict.values():
#         # don't count it as a girl name if no babies were actually given the name
#         if v[gender] > 0:
#             bcount += v[gender]
#             ncount += 1
#     print("    %s:" % gender, ncount, "unique names for", bcount, "babies")
