from os.path import join
import csv
DATA_DIR = 'tempdata'
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled2014.csv')


rfile = open(WRANGLED_DATA_FILENAME, 'r')
datarows = list(csv.DictReader(rfile)) # just make it all a big list of dicts

# because numbers in a CSV file are deserialized/importated
# as plain strings, we need to do some work to re typecast them
# to integers
for r in datarows:
    r['total'] = int(r['total'])
    r['males'] = int(r['males'])
    r['females'] = int(r['females'])
    r['ratio'] = int(r['ratio'])
    # these operations *mutate* the r object, thus
    # every object in datarows has been transformed...but that's cool



# finally print 5 most popular names with less than 60% f/m ratio
# shouldn't have to resort bigdatarows, as it was already presorted
# but if you want to be sure...
print("Most popular names with <= 60% gender skew:")
bigdatarows = sorted(datarows, key=lambda r: r['total'], reverse=True)
fxrows = [r for r in datarows if r['ratio'] <= 60 ]

for row in fxrows[0:5]:
    print(row['name'].ljust(10), row['gender'], row['ratio'], row['total'])
