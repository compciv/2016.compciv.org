from os.path import join
import json
JSON_PATH = join('tempdata', 'googlemaps', 'stanford.json')
# open the file
f = open(JSON_PATH, 'r')
data = json.loads(f.read())
f.close()

print(data['status'])
