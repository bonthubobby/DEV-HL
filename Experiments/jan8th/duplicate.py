
import csv

reader=csv.reader(open('data2.csv', 'r'), delimiter=',')
writer=csv.writer(open('uniquedata2.csv', 'w'), delimiter=',')

lastnames = set()
for row in reader:
    if row[0] not in lastnames:
        writer.writerow(row)
        lastnames.add( row[0] )
print len(lastnames)   
