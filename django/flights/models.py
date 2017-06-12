from django.db import models

#HiddenFlights: Class for items that are unique to details that we don't plan to show on the search page
class HiddenFlight(models.Model):
    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField()
    fl_date = models.DateTimeField()
    carrier = models.CharField(max_length = 2)
    origin_airport_id = models.PositiveIntegerField()
    dest_airport_id = models.PositiveIntegerField()
    dep_delay_new = models.PositiveSmallIntegerField()
    arr_delay_new = models.PositiveSmallIntegerField()
    cancelled = models.PositiveSmallIntegerField()
    diverted = models.PositiveSmallIntegerField()

#DisplayFlights: Class for items unique to items that we will show on the search page
class DisplayFlight(models.Model):
    unique_carrier = models.CharField(max_length = 2)
    fl_num = models.PositiveSmallIntegerField()
    origin = models.CharField(max_length = 3)
    dest = models.CharField(max_length = 3)
