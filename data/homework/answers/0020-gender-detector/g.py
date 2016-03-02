from os.path import join, basename
import csv
DATA_DIR = 'tempdata'
# the "wrangled file" we're going to create will have its own headers
WRANGLED_HEADERS = ['year', 'name', 'gender' , 'ratio' , 'females', 'males', 'total']
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled2014.csv')
# this is same as previous exercises with a single file
YEAR = 2014
thefilename = join(DATA_DIR, 'yob' + str(YEAR) + '.txt')


namesdict = {}
with open(thefilename, 'r') as thefile:
    for line in thefile:
        name, gender, count = line.split(',')
        if not namesdict.get(name): # need to initialize a new dict for the name
            namesdict[name] = {'M': 0, 'F': 0}
        namesdict[name][gender] += int(count)


# Let's make a new list
my_awesome_list = []
# and let's fill it with dicts, from dicts that are in namesdict
for name, babiescount in namesdict.items():
    xdict = {}
    xdict['year'] = YEAR
    xdict['name'] = name
    xdict['females'] = babiescount['F']
    xdict['males'] = babiescount['M']
    xdict['total'] = xdict['males'] + xdict['females']
    # the "likely" gender is determined by comparing females vs males numbers
    if xdict['females'] >= xdict['males']:
        xdict['gender'] = 'F'
        xdict['ratio'] = round(100 * xdict['females'] / xdict['total'])
    else:
        xdict['gender'] = 'M'
        xdict['ratio'] = round(100 * xdict['males'] / xdict['total'])

    # finally, add our new dict, xdict, to my_awesome_list
    my_awesome_list.append(xdict)



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

my_final_list = sorted(my_awesome_list, key=xfoo)

# and now we just iterate through every row and
# add it to wcsv
for row in my_final_list:
    wcsv.writerow(row)
# the end...
wfile.close()


# Ohhh but we're not done yet...we have to print
# the first 5 lines of text (which will include the headers)
# this is just opening a file and printing the line
finalfile = open(WRANGLED_DATA_FILENAME, 'r')
thestupidlines = finalfile.readlines()[0:5]
for line in thestupidlines:
    # remember each text line has a newline character
    # that we don't want to print out for aesthetic reasons
    print(line.strip())

# result
# year,name,gender,ratio,females,males,total
# 2014,Emma,F,100,20799,12,20811
# 2014,Olivia,F,100,19674,22,19696
# 2014,Noah,M,99,106,19144,19250
# 2014,Sophia,F,100,18490,17,18507
