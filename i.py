from os.path import join
import csv
DATA_DIR = 'tempdata'
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled2014.csv')

wrangledfile = open(WRANGLED_DATA_FILENAME, 'r')
datarows = list(csv.DictReader(wrangledfile)) 

for r in datarows:
	r['total'] = int(r['total'])
	r['males'] = int(r['males'])
	r['females'] = int(r['females'])
	r['ratio'] = int(r['ratio'])
print("Popular names with a gender ratio bias of less than or equal to:")

bigdatarows = []
for r in datarows:
	if int(r['total']) >= 100: 
		bigdatarows.append(r)


fxrows= [r for r in bigdatarows if r['ratio']<= 60]
fyrows= [r for r in bigdatarows if r['ratio']<= 70]
fzrows= [r for r in bigdatarows if r['ratio']<= 80]
farows= [r for r in bigdatarows if r['ratio']<= 90]
fbrows= [r for r in bigdatarows if r['ratio']<= 99]


for r in fxrows[0:1]:
	print ("60", (len(fxrows)), "/", len(bigdatarows))
for r in fxrows[1:2]:
	print ("70", (len(fyrows)), "/", len(bigdatarows))
for r in fzrows[2:3]:
	print ("80", (len(fzrows)), "/", len(bigdatarows))
for r in farows[3:4]:
	print ("80", (len(farows)), "/", len(bigdatarows))
for r in fbrows[4:5]:
	print ("80", (len(fbrows)), "/", len(bigdatarows))

# for genderratio in (60, 70, 80, 90, 99):
# 	bigdatarows = sorted(datarows, key=lambda r: r['total'], reverse=True)
# 	print(genderratio, ':', row['ratio'], '/', len(bigdatarows)) 
