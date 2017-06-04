import urllib.request, urllib.error, urllib.parse
import json
from . import key_info
from datetime import datetime

class FlightInfo():

    api_key = key_info.api_key
    app_id = key_info.app_id

    supported_airlines = ['UA', 'AA', 'NK', 'B6', 'WN', 'VX', 'F9', 'CO', 'AS', 'DL']

    if __name__ == '__main__':
        pass

    def get_rating(self, airline, flight_id, departure):
        """
        Get rating of individual flights

        Args:
        airline: string of airline code (i.e. 'AA')
        flight_id: string of flight id number (i.e. '219')
        departure: string of airport code representing departing airport (ie. 'ORD')

        Returns:
        tuple containing rating, departure airport code, and arrival airport code
        """
        url = ("https://api.flightstats.com/flex/ratings/rest/v1/json/flight/"
        "{0}/{1}?appId={2}&appKey={3}&departureAirport={4}"
        .format(airline, flight_id, self.app_id, self.api_key, departure))
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        if 'ratings' in list(data.keys()):
            #check if too little data on flight
            if int(data['ratings'][0]['observations']) < 5:
                return None
            rating = int(data['ratings'][0]['allOntimeCumulative']*100)
            departure = data['appendix']['airports'][0]['fs']
            arrival = data['appendix']['airports'][1]['fs']
            return (rating, departure, arrival)
        return None
    def get_flights(self, departure, arrival):
        """
        Get flights running on specified route and gather their ratings

        Args:
        arrival: string of airport code representing arrival airport (ie. 'ORD')
        departure: string of airport code representing departing airport

        Returns:
        list of tuples containing airline, flight_id, and rating
        """
        today = datetime.today()
        url = ("https://api.flightstats.com/flex/schedules/rest/v1/json/from/"
        "{0}/to/{1}/departing/{2}/{3}/{4}?appId={5}&appKey={6}"
        .format(departure, arrival, today.year, today.month, today.day, self.app_id, self.api_key))
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        flight_ratings = []
        for flight in data['scheduledFlights']:
            airline = flight['carrierFsCode']
            #skip unsupported airlines
            if airline not in self.supported_airlines:
                continue
            flight_id = flight['flightNumber']
            rating = self.get_rating(airline, flight_id, departure)
            if rating is not None:
                rating = rating[0]
                flight_ratings.append((airline, flight_id, rating))
        return flight_ratings
