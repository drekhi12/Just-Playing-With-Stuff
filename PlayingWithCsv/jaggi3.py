import csv
import collections

columns = collections.defaultdict(list)
with open('some.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    with open('some2.csv', 'wb') as f:
		writer = csv.writer(f)
		specials = '\"'
		length_of_row = []
		for row in reader:
			row= [value.replace(specials,'') for value in row]
			length_of_row.append(len(row))
			writer.writerow(row)
			for (i,v) in enumerate (row):
				columns[i].append(v) 
		print length_of_row
	
# for s in range(2,3):
for i in range(1,39):
	print i
	print  columns[i][1]
	print "======================================="
# 		# 	#writer.writerow(row)
