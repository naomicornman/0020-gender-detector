from os.path import join, basename
YEAR = 2014
DATA_DIR = 'tempdata'
yearfilename = join(DATA_DIR, 'yob' + str(YEAR) + '.txt')
names_dict = {}
thefile =  open(yearfilename, 'r')
for line in thefile:
    name, gender, count = line.split(',')
    if not names_dict.get(name):
    	names_dict[name] = {'M': 0, 'F': 0}
    names_dict[name][gender] += int(count)
    

totalnamecount = len(names_dict.keys())
totalbabycount = 0

for v in names_dict.values():
	allbabies = v['M'] + v['F']
	totalbabycount += allbabies

print("Total:", totalnamecount, 'unique names for', totalbabycount, 'babies')

ncount = 0
bcount = 0
for v in names_dict.values():
	if v['M'] > 0:
		bcount += v['M']
		ncount += 1
print("    M:", ncount, "unique names for", bcount, "babies")

ncount = 0
bcount = 0
for v in names_dict.values():
    if v['F'] > 0:
        bcount += v['F']
        ncount += 1
print("    F:", ncount, "unique names for", bcount, "babies")


