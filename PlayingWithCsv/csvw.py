import csv
import collections

columns = collections.defaultdict(list)
with open('some1.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
    	for (i,v) in enumerate (row):
    		columns[i].append(v) 



with open('some1.csv') as f:
    reader = csv.reader(f, delimiter=' ', skipinitialspace=True)
    length_of_row=[]
    for f in reader:
    	length_of_row.append(len(f))

length_of_row.insert(0,33)
for i in range(0,101):
	print i
	print length_of_row[i]
	print "=============================="


