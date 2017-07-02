from django.db import models

class Flight(models.Model):
    fl_date = models.DateTimeField()
    carrier = models.CharField(max_length = 2)
    origin_airport_id = models.PositiveIntegerField()
    dest_airport_id = models.PositiveIntegerField()
    dep_delay_new = models.PositiveSmallIntegerField()
    arr_delay_new = models.PositiveSmallIntegerField()
    cancelled = models.PositiveSmallIntegerField()
    diverted = models.PositiveSmallIntegerField()
    unique_carrier = models.CharField(max_length = 2)
    fl_num = models.PositiveSmallIntegerField()
    origin = models.CharField(max_length = 3)
    dest = models.CharField(max_length = 3)
    OTR = models.PositiveSmallIntegerField()


#DisplayFlights: Class for items unique to items that we will show on the search page
class DisplayFlight(models.Model):
    unique_carrier = models.CharField(max_length = 2)
    fl_num = models.PositiveSmallIntegerField()
    origin = models.CharField(max_length = 3)
    dest = models.CharField(max_length = 3)
    OTR = models.PositiveSmallIntegerField()
    scheduled_departure_time = models.PositiveSmallIntegerField() #24 hour time
    scheduled_arrival_time = models.PositiveSmallIntegerField() #24 hour time
