from os.path import join, basename
import csv
DATA_DIR = 'tempdata'
WRANGLED_HEADERS = ['name', 'gender' , 'ratio' , 'females', 'males', 'total']
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangledbabynames.csv')

wrangledfile = open(WRANGLED_DATA_FILENAME, 'r')
datarows = list(csv.DictReader(wrangledfile)) 

for r in datarows:
    r['total'] = int(r['total'])
    r['males'] = int(r['males'])
    r['females'] = int(r['females'])
    r['ratio'] = int(r['ratio'])

def detect_gender_from_csv(name):
    result = { 'name': name, 'gender': 'NA', 'ratio': None, 'males': None, 'females': None, 'total': 0 }
    for row in datarows:
        if name.lower() == row['name'].lower():
            result = row
            break
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


# bigdatarows = []

# for r in datarows:
#     if r['name'] == "Michael": 
#         print (r['name'],r['gender'],r['ratio'])
#     if r['name'] == "Kelly": 
#         print (r['name'],r['gender'],r['ratio'])
#     if r['name'] == "Kanye": 
#         print (r['name'],r['gender'],r['ratio'])
#     if r['name'] == ("THOR"): 
#         print (r['name'],r['gender'],r['ratio'])
   

#     if r['name'] == str("casey"): 
#         print (r['name'],r['gender'],r['ratio'])
#     if r['name'] == "Arya": 
#         print (r['name'],r['gender'],r['ratio'])
#     if r['name'] == "ZZZblahblah": 
#         print (r['name'],r['gender'],r['ratio'])


