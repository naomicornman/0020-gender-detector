from os.path import join
import json
import csv
DATA_DIR = 'tempdata'
WRANGLED_CSV_FILENAME = join(DATA_DIR, 'wrangledbabynames.csv')
WRANGLED_JSON_FILENAME = join(DATA_DIR, 'wrangledbabynames.json')
with open(WRANGLED_CSV_FILENAME, 'r') as rfile:
    datarows = list(csv.DictReader(rfile)) 
for r in datarows:
    r['total'] = int(r['total'])
    r['males'] = int(r['males'])
    r['females'] = int(r['females'])
    r['ratio'] = int(r['ratio'])

whateverfile = open(WRANGLED_JSON_FILENAME, 'w')
jsontext = json.dumps(datarows, indent=2)
whateverfile.write(jsontext)
whateverfile.close()

csvtxt = open(WRANGLED_CSV_FILENAME).read()
jsontxt = open(WRANGLED_JSON_FILENAME).read()

print("CSV has", len(csvtxt), "characters")
print("JSON has", len(jsontxt), "characters")

size_ratio = round(((len(jsontxt) - len(csvtxt)) / len(csvtxt)), 1)
print("JSON requires", size_ratio, "times more text characters than CSV")