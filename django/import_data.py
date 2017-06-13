import sys
import os
import django
# from django.core.management import setup_environ
sys.path.append('/django')

'''this is a depreciated way'''
#from airontime import settings
#setup_environ(settings)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "airontime.settings")
django.setup()

from flights.models import Flight
import csv


with open('sanitized_flight_data.csv') as f:
    reader = csv.reader(f)
    count = 0
    for row in reader:
        count+=1
        print(count)
        _, created = Flight.objects.get_or_create(
            year = row[0],
            month = row[1],
            fl_date = row[2],
            unique_carrier = row[3],
            carrier = row[4],
            fl_num = row[5],
            origin_airport_id = row[6],
            origin = row[7],
            dest_airport_id = row[8],
            dest = row[9],
            dep_delay_new = row[10],
            arr_delay_new = row[11],
            cancelled = row[12],
            diverted = row[13],
            OTR = 0
        )




'''
dataReader = csv.reader(open('sanitized_flight_data.csv'), delimiter=',')
count = 0

for row in dataReader:
    count+=1
    print(count)
    DisplayFlight = DisplayFlight()
    DisplayFlight.unique_carrier = row[3]
    DisplayFlight.fl_num = row[5]
    DisplayFlight.origin = row[7]
    DisplayFlight.dest = row[9]
    DisplayFlight.OTR = 0
    DisplayFlight.save()


dataReader = csv.reader(open('sanitized_flight_data.csv'), delimiter=',')
count = 0

for row in dataReader:
    count+=1
    print(count)
    HiddenFlight = HiddenFlight()
    HiddenFlight.year = row[0]
    HiddenFlight.month = row[1]
    HiddenFlight.fl_date = row[2]
    HiddenFlight.carrier = row[4]
    HiddenFlight.origin_airport_id = row[6]
    HiddenFlight.dest_airport_id = row[8]
    HiddenFlight.dep_delay_new = row[10]
    HiddenFlight.arr_delay_new = row[11]
    HiddenFlight.cancelled = row[12]
    HiddenFlight.diverted = row[13]
    HiddenFlight.save()

'''
