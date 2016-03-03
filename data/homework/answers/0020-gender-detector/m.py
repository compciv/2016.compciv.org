from os.path import join
import json
import csv
DATA_DIR = 'tempdata'
WRANGLED_CSV_FILENAME = join(DATA_DIR, 'wrangledbabynames.csv')
WRANGLED_JSON_FILENAME = join(DATA_DIR, 'wrangledbabynames.json')
# last time we open this
with open(WRANGLED_CSV_FILENAME, 'r') as rfile:
    datarows = list(csv.DictReader(rfile)) # just make it all a big list of dicts
# same routine to convert strings to numbers
for r in datarows:
    r['total'] = int(r['total'])
    r['males'] = int(r['males'])
    r['females'] = int(r['females'])
    r['ratio'] = int(r['ratio'])
# now, we serialize as json

# first, open the JSON file, just like any old file to write to:
whateverfile = open(WRANGLED_JSON_FILENAME, 'w')
# then we serialize datarows into JSON, i.e.
# convert that list of dictionaries into just plaintext that is
#  formatted like the JSON spec
jsontext = json.dumps(datarows, indent=2)
# then we write it to file object
whateverfile.write(jsontext)
# and then we close that file object
whateverfile.close()


# Now, print the difference in character count between the two file formats
csvtxt = open(WRANGLED_CSV_FILENAME).read()
jsontxt = open(WRANGLED_JSON_FILENAME).read()
# remember, without the json or csv modules being called
# both of these things are just raw text
print("CSV has", len(csvtxt), "characters")
print("JSON has", len(jsontxt), "characters")
# let's calculate how many times bigger the character increase is
size_ratio = round(((len(jsontxt) - len(csvtxt)) / len(csvtxt)), 1)
print("JSON requires", size_ratio, "times more text characters than CSV")
