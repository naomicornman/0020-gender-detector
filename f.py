from os.path import join, basename
from glob import glob
DATA_DIR = 'tempdata'
START_YEAR = 1950
END_YEAR = 2015

for year in range(START_YEAR, END_YEAR, 5):
    yearfilename = join(DATA_DIR, 'yob' + str(year) + '.txt')
    names_dict = {}
    thefile =  open(yearfilename, 'r')

    for line in thefile:
        name, gender, count = line.split(',')
    if not names_dict.get(name):
        names_dict[name] = {'M': 0, 'F': 0}
    names_dict[name][gender] += int(count)
    thefile.close()

    print (year)
    totalnamecount = len(names_dict.keys())
    totalbabycount = sum(v['F'] * v['M'] for v in names_dict.values())
    print("Total:", round(totalbabycount / totalnamecount), 'babies per name')
# for boys and girls separately
    for gd in ['M', 'F']:
        babyct = 0
        namect = 0
        for v in names_dict.values():
            if v[gd] > 0:
                babyct += v[gd]
                namect += 1
        print("    %s:" % gd, round(babyct / namect), 'babies per name')