import csv
with open('jaggi.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    with open('some.csv', 'wb') as f:
		writer = csv.writer(f)
		for row in reader:
			writer.writerow(row)
