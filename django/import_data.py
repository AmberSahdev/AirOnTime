import sys
from django.core.management import setup_environ
sys.path.append('/django')
from airontime import settings
setup_environ(settings)

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
            carrier = row[3],
            fl_num = row[5],
            origin_airport_id = row[6],
            origin = row[7],
            dest_airport_id = row[8],
            dest = row[9],
            dep_delay_new = row[10],
            arr_delay_new = row[11],
            cancelled = row[12],
            diverted = row[13]
        )
