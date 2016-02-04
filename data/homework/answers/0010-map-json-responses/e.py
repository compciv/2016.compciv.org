from os.path import join
import json
JSON_PATH = join('tempdata', 'googlemaps', 'stanford.json')
# open the file
f = open(JSON_PATH, 'r')
data = json.loads(f.read())
f.close()


for result in data['results']:
    mylist = []
    mylist.append(result['formatted_address'])
    mylist.append(str(result['geometry']['location']['lng']))
    mylist.append(str(result['geometry']['location']['lat']))
    print( ';'.join(mylist) )
