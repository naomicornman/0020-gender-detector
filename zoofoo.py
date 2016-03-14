from os.path import join
import json
DATA_DIR = 'tempdata'
WRANGLED_JSON_FILENAME = join(DATA_DIR, 'wrangledbabynames.json')

NAMES_DATA_ROWS = json.load(open(WRANGLED_JSON_FILENAME))

# wrangledfile = open(WRANGLED_JSON_FILENAME, 'r')
# datarows = list(csv.DictReader(wrangledfile)) 

def detect_gender(name):

    result = { 'name': name, 'gender': None, 'ratio': None, 'males': 0, 'females': 0, 'total': 0 }
    for row in NAMES_DATA_ROWS:
        if name.lower() == row['name'].lower():
            result = row
            break
    return result

NAMES_TO_TEST = ['Michael', 'Kelly', 'Kanye', 'THOR', 'casey', 'Arya', 'ZZZblahblah']
namecount = {'M': 0, 'F': 0, 'NA': 0}
babycount = {'males': 0, 'females': 0}


for name in NAMES_TO_TEST:
    result = detect_gender(name)
    print(name, result['gender'], result['ratio'])
    if result['gender']:
        namecount[result['gender']] += 1

    if result['gender'] != 'NA':  # we don't want to count the NA's
        babycount['males'] += result['males']
        babycount['females'] += result['females']

print("Total:")
print("F:", namecount['F'], 'M:', namecount['M'], 'NA:', namecount['NA'])
print('females:', babycount['females'], 'males:', babycount['males'])