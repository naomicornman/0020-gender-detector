from os.path import join, basename
from glob import glob
DATA_DIR = 'tempdata'

# unlike b.py, this simply keeps a count of "names", not total babies
tally = {'M': set(), 'F': set()}

for fname in glob(join(DATA_DIR, '*.txt')):
    # doing the filtering if filenames in one loop
    year = basename(fname)[3:7]
    if year >= "1950":
        for line in open(fname, 'r'):
            name, gender, babies = line.split(',')
            tally[gender].add(name)

print("F:", str(totalsdict['F']).rjust(5),
	"M:", str(totalsdict['M']).rjust(5))

f_to_m_ratio = round(100 * totalsdict['F'] / totalsdict['M'])
print("F/M baby ratio:", f_to_m_ratio)