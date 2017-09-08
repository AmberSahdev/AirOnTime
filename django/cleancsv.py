#Step 1 after getting csv with data
#cleans the csv data
import csv

supported_airlines = ['AA', 'UA', 'AS', 'DL', 'F9', 'B6', 'WN', 'NK', 'VX', 'AC', 'CO', 'G4', 'HA', 'MQ', 'OO']

with open('raw_data/01_2017_BTS_ONTIME.csv') as f: #replace 01_2017_BTS_ONTIME.csv with your file name
    reader = csv.reader(f)
    #skip header
    next(reader, None)

    writer = csv.writer(open("clean_data/clean_01_2017_BTS_ONTIME", "wb")) #replace 01_2017_BTS_ONTIME.csv with your file name

    for row in reader:
        #remove rows with empty strings or that contain unsupported airlines
        row = filter(None, row)

        if len(row) == 9 and row[1] in supported_airlines:
            writer.writerow(row)
            
