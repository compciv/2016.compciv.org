from os.path import join
import json
JSON_PATH = join('tempdata', 'mapzen', 'stanford.json')
# open the file
f = open(JSON_PATH, 'r')
data = json.loads(f.read())
f.close()


for feature in data['features']:
    datum = []
    datum.append(feature['properties']['label'])
    datum.append(feature['properties']['confidence'])
    coords = feature['geometry']['coordinates']
    datum.extend(coords)

    print(';'.join([str(d) for d in datum]))
