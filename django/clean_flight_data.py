import csv

rows = []

supported_airlines = ['AA', 'UA', 'AS', 'DL', 'F9', 'B6', 'WN', 'NK', 'VX', 'AC', 'CO', 'G4', 'HA', 'MQ', 'OO']

with open('january.csv') as f:
    reader = csv.reader(f)
    #skip header
    next(reader, None)
    for row in reader:
        #remove rows with empty strings or that contain unsupported airlines
        row = filter(None, row)
        if len(row) == 14 and row[3] in supported_airlines:
            row[10] = int(float(row[10]))
            row[11] = int(float(row[11]))
            row[12] = int(float(row[12]))
            row[13] = int(float(row[13]))
            rows.append(row)

writer = csv.writer(open("january_sanitized_flight_data.csv", "wb"))
print len(rows)
for row in rows:
    writer.writerow(row)
