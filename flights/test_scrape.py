from fs_api import Flights

flights = Flights()
rating = flights.get_rating('UA', '225', 'ORD')
print(rating)
