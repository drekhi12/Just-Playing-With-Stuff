import csv
with open('jaggi.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    with open('some.csv', 'wb') as f:
		writer = csv.writer(f)
		specials='\"'
		for row in reader:
			row= [value.replace(specials,'') for value in row]
			writer.writerow(row)
