from os.path import join, basename
import csv
DATA_DIR = 'tempdata'
# as before, we create new headers for our wrangled file
# though we leave out year because we probably don't care at for our ultimate needs
WRANGLED_HEADERS = ['name', 'gender' , 'ratio' , 'females', 'males', 'total']
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangledbabynames.csv')
START_YEAR = 1950
END_YEAR = 2014
# lets just get a list of all decades, between 1950 and 2014:
years = list(range(START_YEAR, END_YEAR, 10))
# and let's tack on the END_YEAR manually:
years.append(END_YEAR)

# namesdict sees all names
namesdict = {}
for year in years:
    # get the file for this particular year
    filename = join(DATA_DIR, 'yob' + str(year) + '.txt')
    print("Parsing", filename)
    # open that file, read it completely in mydict
    with open(filename, 'r') as thefile:
        for line in thefile:
            name, gender, count = line.split(',')
            if not namesdict.get(name): # need to initialize a dict for this name
                namesdict[name] = {'F': 0, 'M': 0}
            # unlike in past exercises, because we're reading multiple years
            # we will be adding to these dicts more than twice (i.e. M and F, and for every year combo)
            # so mind that += operator
            namesdict[name][gender] += int(count)

# Wait till every year is done
my_awesome_list = []
# just the same as it was for g.py, except no "year"
for name, babiescount in namesdict.items():
    xdict = {'name': name, 'females': babiescount['F'], 'males': babiescount['M']}
    xdict['total'] = xdict['males'] + xdict['females']
    if xdict['females'] >= xdict['males']:
        xdict['gender'] = 'F'
        xdict['ratio'] = round(100 * xdict['females'] / xdict['total'])
    else:
        xdict['gender'] = 'M'
        xdict['ratio'] = round(100 * xdict['males'] / xdict['total'])
    # finally, add our new dict, xdict, to my_awesome_list
    my_awesome_list.append(xdict)


# totally the same as g.py

# let's create the new file to write to
wfile = open(WRANGLED_DATA_FILENAME, 'w')
# turn it into a DictWriter object, and tell it what the fieldnames are
wcsv = csv.DictWriter(wfile, fieldnames=WRANGLED_HEADERS)
# write the headers row
wcsv.writeheader()

# before we start adding the contents of my_awesome_list to
# wcsv, we want to sort it in order of:
#  - descending total
#  - ascending name
# here's one way to do it, make a silly little function:
def xfoo(xdict):
    # and return a tuple of negative total, and normal name
    return (-xdict['total'], xdict['name'])

# and now we just iterate through every row and
# add it to wcsv
for row in sorted(my_awesome_list, key=xfoo):
    wcsv.writerow(row)
# the end...
wfile.close()


# Ohhh but we're not done yet...we have to print
# the first 5 lines of text (which will include the headers)
# this is just opening a file and printing the line
with open(WRANGLED_DATA_FILENAME, 'r') as f:
    for line in f.readlines()[0:5]:
        print(line.strip())

# Parsing tempdata/yob1950.txt
# Parsing tempdata/yob1960.txt
# Parsing tempdata/yob1970.txt
# Parsing tempdata/yob1980.txt
# Parsing tempdata/yob1990.txt
# Parsing tempdata/yob2000.txt
# Parsing tempdata/yob2010.txt
# Parsing tempdata/yob2014.txt
# name,gender,ratio,females,males,total
# Michael,M,100,1963,433277,435240
# James,M,100,1391,342651,344042
# David,M,100,1139,330092,331231
# John,M,100,1095,320621,321716
