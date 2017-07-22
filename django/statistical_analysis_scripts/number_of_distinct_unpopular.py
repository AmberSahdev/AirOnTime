import csv

unpopular_seen = set()
popular_seen = set()

unpopular_airlines = ['AS', 'B6', 'AC', 'CO', 'G4', 'HA', 'MQ', 'OO', 'VX']
popular_airlines = ['AA', 'UA', 'DL', 'F9', 'WN', 'NK']


with open('january_sanitized_flight_data.csv') as f:
    reader = csv.reader(f)

    unpopular_count = 0
    popular_count = 0
    for row in reader:
        row = filter(None, row)
        key = (row[4], row[5], row[7], row[9])
        if row[4] in unpopular_airlines and key not in unpopular_seen:
            unpopular_seen.add(key)
            unpopular_count += 1
        if row[4] in popular_airlines and key not in popular_seen:
            popular_seen.add(key)
            popular_count += 1


    print(unpopular_count)
    print('^ this is the number of distinct unpopular flights')
    print(popular_count)
    print('^ this is the number of distinct popular flights')

    f.close()
