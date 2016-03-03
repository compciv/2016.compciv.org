from os.path import join
import csv
DATA_DIR = 'tempdata'
WRANGLED_FINAL_FILENAME = join(DATA_DIR, 'wrangledbabynames.csv')
# boy this is bad practice...but it's fast...
NAMES_DATA_ROWS = list(csv.DictReader(open(WRANGLED_FINAL_FILENAME)))
# as before, we need to manually typecast certain fields to numbers
# because CSV just thinks everything is all a bunch of text characters:
for r in NAMES_DATA_ROWS:
    r['total'] = int(r['total'])
    r['males'] = int(r['males'])
    r['females'] = int(r['females'])
    r['ratio'] = int(r['ratio'])


def detect_gender_from_csv(name):
    # prepare an empty result just in case the given name is not found in our database
    result = { 'name': name, 'gender': 'NA', 'ratio': None, 'males': None, 'females': None, 'total': 0 }
    for row in NAMES_DATA_ROWS:
        # find first row...
        if name.lower() == row['name'].lower():
            # this should be the match
            result = row
            # since each name only shows up once in our list
            # we can break early rather than iterating through the rest of NAMES_DATA_ROWS
            break
    # if no match was found, result is what it was at the beginning
    return result



NAMES_TO_TEST = ['Michael', 'Kelly', 'Kanye', 'THOR', 'casey', 'Arya', 'ZZZblahblah']


namecount = {'M': 0, 'F': 0, 'NA': 0}
babycount = {'males': 0, 'females': 0}
for name in NAMES_TO_TEST:
    result = detect_gender_from_csv(name)
    print(name, result['gender'], result['ratio'])
    if result['gender']:
        namecount[result['gender']] += 1

    if result['gender'] != 'NA':  # we don't want to count the NA's
        babycount['males'] += result['males']
        babycount['females'] += result['females']

print("Total:")
print("F:", namecount['F'], 'M:', namecount['M'], 'NA:', namecount['NA'])
print('females:', babycount['females'], 'males:', babycount['males'])
