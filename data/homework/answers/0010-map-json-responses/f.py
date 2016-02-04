from os.path import join
import json
JSON_PATH = join('tempdata', 'mapzen', 'stanford.json')
# open the file
f = open(JSON_PATH, 'r')
data = json.loads(f.read())
f.close()


query_dict = data['geocoding']['query']

for key in ['text', 'size', 'boundary.country']:
    print(key + ':', query_dict[key])
