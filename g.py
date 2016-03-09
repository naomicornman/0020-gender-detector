from os.path import join, basename
import csv
DATA_DIR = 'tempdata'
YEAR = 2014
thefilename = join(DATA_DIR, 'yob' + str(YEAR) + '.txt')

WRANGLED_HEADERS = ['year', 'name', 'gender' , 'ratio' , 'females', 'males', 'total']
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled2014.csv')

namesdict = {}
with open(thefilename, 'r') as thefile:
    for line in thefile:
        name, gender, count = line.split(',')
        if not namesdict.get(name):
            namesdict[name] = {'M': 0, 'F': 0}
        namesdict[name][gender] += int(count)

newlist = []

for name, counts in namesdict.items():
    xdict = {}
    xdict['year'] = YEAR # i.e. 2014
    xdict['name'] = name
    xdict['females'] = counts['F']
    xdict['males'] = counts['M']
    xdict['total'] = xdict['males'] + xdict['females']
    if xdict['females'] >= xdict['males']:
        xdict['gender'] = 'F'
        xdict['ratio'] = round(100 * xdict['females'] / xdict['total'])
    else:
        xdict['gender'] = 'M'
        xdict['ratio'] = round(100 * xdict['males'] / xdict['total'])
    newlist.append(xdict)

wfile = open(WRANGLED_DATA_FILENAME, 'w')
wcsv = csv.DictWriter(wfile, fieldnames=WRANGLED_HEADERS)
wcsv.writeheader()

def xdata(xdict):
    return (-xdict['total'], xdict['name'])

my_final_list = sorted(newlist, key=xdata)
for row in my_final_list:
    wcsv.writerow(row)
wfile.close()

finalfile = open(WRANGLED_DATA_FILENAME, 'r')
thestupidlines = finalfile.readlines()[0:5]
for line in thestupidlines:
	 print(line.strip())



