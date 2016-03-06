from os.path import join, basename
from glob import glob
DATA_DIR = 'tempdata'

for fname in glob(join(DATA_DIR, '*.txt')):
    year = basename(fname)[3:7]
    tally = {'M': set(), 'F': set()}
    if year >= "1950":
    	print (year)
    	for line in open(fname, 'r'):
    		name, gender, babies = line.split(',')
    		tally[gender].add(name)
    	print("F:", len(tally['F']),
			"M:", len(tally['M']))
    	f_to_m_ratio = round(100 * len(tally['F']) / len(tally['M']))
    	print("F/M baby ratio:", f_to_m_ratio)