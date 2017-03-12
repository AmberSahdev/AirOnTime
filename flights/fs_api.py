import urllib2
import json
import key_info

#curl -v  -X GET "https://api.flightstats.com/flex/schedules/rest/v1/json/from/ORD/to/ATL/departing/2017/3/13?appId=677a5145&appKey=b8d6a7a9160973f9c01c6ad702ea918c"
class Flights():

    api_key = key_info.api_key
    app_id = key_info.app_id

    def get_rating(self, airline, flight_id, departure):
        url = ("https://api.flightstats.com/flex/ratings/rest/v1/json/flight/"
        "{0}/{1}?appId={2}&appKey={3}&departureAirport={4}"
        .format(airline,flight_id,self.app_id,self.api_key,departure))
        print(url)
        response = urllib2.urlopen(url)
        data = json.loads(response.read())
        if 'ratings' in data.keys():
            rating = data['ratings'][0]['allOntimeCumulative']*100
            departure = data['appendix']['airports'][0]['fs']
            arrival = data['appendix']['airports'][1]['fs']
            return (rating,departure,arrival)
        return None
    def get_flights(self, departure, arrivals):
        pass
