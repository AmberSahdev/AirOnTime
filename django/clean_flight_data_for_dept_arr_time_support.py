import csv

seen = set()

supported_airlines = ['AA', 'UA', 'AS', 'DL', 'F9', 'B6', 'WN', 'NK', 'VX', 'AC', 'CO', 'G4', 'HA', 'MQ', 'OO']

with open('downloaded_scheduled_dept_and_arr_data.csv') as f:
    reader = csv.reader(f)
    #skip header
    next(reader, None)

    writer = csv.writer(open("departure_and_arrival_times.csv", "wb"))

    for row in reader:
        #remove rows with empty strings or that contain unsupported airlines
        row = filter(None, row)
        key = (row[1], row[2], row[3], row[4])
        if len(row) == 7 and row[1] in supported_airlines and key not in seen:
            writer.writerow(row)
            seen.add(key)
