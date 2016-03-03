from os.path import join, basename
from glob import glob
DATA_DIR = 'tempdata'
alltxtfiles_path = join(DATA_DIR, '*.txt')
alltxtfiles_names = glob(alltxtfiles_path)

a_filename = 'tempdata/yob1951.txt'
bname = basename(a_filename)
year = bname[3:7]

myfilenames = []
for fname in alltxtfiles_names:
  bname = basename(fname) 
  year = bname[3:7]       
  if year >= "1950":
      myfilenames.append(fname)

totalsdict = {'M': 0, 'F': 0}

for fname in myfilenames:
    babyfile = open(fname, "r")
    for line in babyfile:
        name, gender, babies = line.split(',')
        totalsdict[gender] += int(babies)

print("F:", str(totalsdict['F']).rjust(5),
      "M:", str(totalsdict['M']).rjust(5))


F_to_M_ratio = round(100 * totalsdict['F'] / totalsdict['M'])
print("F/M baby ratio:", f_to_m_ratio)