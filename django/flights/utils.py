from fs_api import FlightInfo

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
           'VX' : 'Virgin Atlantic'
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
           'VX' : 'https://www.virginatlantic.com'
           }
    return urls[short]

def get_search_info(airline, flight_id, departure):
    """
    Builds list of information that is to be displayed on search page

    Args:
    airline: string of airline code (i.e. 'AA')
    flight_id: string of flight id number (i.e. '219')
    departure: string of airport code representing departing airport (ie. 'ORD')

    Returns:
    List of lists with airline code, flight number, rating, airline name, and url
    for each respective flight in search results
    """
    flight_info = FlightInfo()
    rating = flight_info.get_rating(airline, flight_id, departure)
    print rating
    if rating is None:
        return None, None

    flights = flight_info.get_flights(rating[1],rating[2])

    results = []
    for flight in flights:
        flight = list(flight)
        full_name = to_full_name(flight[0])
        url = get_url(flight[0])
        flight.append(full_name)
        flight.append(url)
        results.append(flight)
        print sorted(results,key=lambda x: x[2], reverse=True)
    return rating[0], sorted(results,key=lambda x: x[2], reverse=True)
