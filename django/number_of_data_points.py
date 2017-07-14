#script to check how many flights there are in the data that are run by unpopular airlines, and how many total data points
import csv

rows = []

unpopular_airlines = ['AS', 'B6', 'AC', 'CO', 'G4', 'HA', 'MQ', 'OO', 'VX']

with open('sanitized_flight_data.csv') as f:
    reader = csv.reader(f)
    #skip header
    next(reader, None)
    count = 0
    total = 0
    for row in reader:
        row = filter(None, row)
        total+= 1
        if row[4] in unpopular_airlines:
            count +=1

    print(count)
    print('^ this is the number of unpopular data points')
    print(total-count)
    print('^ this is the number of popular data points')
    print(total)
    print('^ this is the number of total data points')
