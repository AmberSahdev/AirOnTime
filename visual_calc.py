import sys
import os
import django

import matplotlib.pyplot as plt

"""
sys.path.append('/django')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "airontime.settings")
django.setup()
"""

popular_airlines = ['AA', 'UA', 'DL', 'F9', 'WN', 'NK']


from flights.models import Flight
unique_flights = set(Flight.objects.all().values_list('carrier', 'fl_num', 'origin', 'dest'))

print(len(unique_flights))

lengths = []
count = 0
while(1):
    count+=1
    print(count)
    try:
        flight = unique_flights.pop()
        if flight[0] in popular_airlines:
            flights = Flight.objects.all().filter(carrier=flight[0], fl_num=flight[1], origin=flight[2], dest=flight[3])
            lengths.append(len(flights))
    except KeyError:
        break

plt.hist(lengths)

plt.savefig('figure.png')
