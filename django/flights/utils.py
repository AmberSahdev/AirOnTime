from flights.models import DisplayFlight

#a collection of utility functions to be used in views.py
def to_full_name(short):
    names = {'AA' : 'American Airlines',
           'UA' : 'United Airlines',
           'AS' : 'Alaska Airlines',
           'DL' : 'Delta Airlines',
           'F9' : 'Frontier Airlines',
           'B6' : 'Jet Blue Airlines',
           'WN' : 'SouthWest Airlines',
           'NK' : 'Spirit Airlines',
           'VX' : 'Virgin Atlantic',
           'AC' : 'Air Canada',
           'CO' : 'Continental Airlines',
           'G4' : 'Allegiant Air',
           'HA' : 'Hawaiian Airlines',
           'MQ' : 'Envoy Air',
           'OO' : 'SkyWest Airlines'
           }
    return names[short]

def get_url(short):
    urls = {'AA' : 'https://www.aa.com',
           'UA' : 'https://www.united.com',
           'AS' : 'https://www.alaskaair.com',
           'DL' : 'https://www.delta.com',
           'F9' : 'https://www.flyfrontier.com',
           'B6' : 'https://www.jetblue.com',
           'WN' : 'https://www.southwest.com',
           'NK' : 'https://www.spirit.com',
           'VX' : 'https://www.virginatlantic.com',
           'AC' : '',
           'CO' : '',
           'G4' : '',
           'HA' : '',
           'MQ' : '',
           'OO' : ''
           }
    return urls[short]


def get_search_info(airline, flight_id, departure, arrival):
    """
    Builds list of information that is to be displayed on search page

    Args:
    airline: string of airline code (i.e. 'AA')
    flight_id: string of flight id number (i.e. '219')
    departure: string of airport code representing departing airport (ex. 'ORD')
    arrival: string of airport code representing arriving airport (ex. 'SFO')

    Returns:
    a tuple with 1st item the rating of the entered flight and second item a list of secondary flights: i.e. other suggested flights
    """
    #requested_flight_rating = primary flight rating = flight that user requested
    #secondary_flights = flights that AOT suggests

    try:
        requested_flight_rating = DisplayFlight.objects.get(unique_carrier = airline, fl_num = flight_id, origin = departure, dest = arrival)
    except:
        return None, None

    secondary_flights = DisplayFlight.objects.filter(origin = departure).filter(dest = arrival)
    secondary_results = []

    for flight in secondary_flights:
        flight = list(flight)
        full_name = to_full_name(flight.unique_carrier)
        url = get_url(flight.unique_carrier)
        flight.append(full_name)
        flight.append(url)
        secondary_results.append(flight)

    return requested_flight_rating.OTR, sorted(secondary_results,key=lambda x: x[2], reverse=True)
