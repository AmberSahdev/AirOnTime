import mechanize
from operator import itemgetter
from BeautifulSoup import BeautifulSoup
from datetime import datetime

import utils

class Scraper():
    br = mechanize.Browser()
    #list of supported airlines
    supported_airlines = ['UA', 'AA', 'NK', 'B6', 'WN', 'VX', 'F9', 'CO', 'AS', 'DL']

    def __init__(self):
        self.initialize_browser()

    def initialize_browser(self):
        br = self.br
        #mimic browser
        br.set_handle_equiv(True)
        br.set_handle_gzip(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    def scrape_flight_info(self, *args):
        br = self.br
        if len(args) == 2:
            br.open('http://www.flightstats.com/go/Home/home.do')

            br.select_form('widgetFlightStatusByFlightForm')

            br.form['airline'] = args[0]
            br.form['flightNumber'] = args[1]

            content = br.submit()

            html = content.read()
        elif len(args) == 1:
            response = br.open(args[0])
            html = response.read()
            print response.geturl()
        else:
            return None, None

        soup = BeautifulSoup(html)

        if soup.find('h1').text == 'Pick Your Flight':
            return None, None
        if len(soup.findAll('div', {'class': 'unknownFlightDesc'})) == 0:
            # rating = soup.findAll('td', valign='top')[1].findAll('td')[18].text
            print br.geturl()
            elements = soup.findAll('td', valign='top')[1].findAll('td')

            rating = None
            for element in elements:
                if len(element.findAll('span', {'class': 'starRating50x9'})) > 0:
                    rating = element.text
            # rating = elements[len(elements)-2].text
            reliability = None
            # if rating.endswith('What\'s this?') and not rating.startswith('No rating available'):
            if rating is not None:
                rating = (float)(rating.split(' ')[0])
                reliability = rating/5.0
                print reliability
                reliability = (int)(reliability*100)
                #round up to 10
                if reliability < 10:
                    reliability = 10
            times = soup.findAll('td', {'class': 'statusValue'})
            depart = times[0].text.split()
            # arrive = times[1].text.split()
            depart.remove('-')
            # arrive.remove('-')
            depart_time = datetime.strptime(depart[0] + depart[1] + depart[2], '%I:%M%p%a')
            # arrive_time = datetime.strptime(arrive[0] + arrive[1] + arrive[2], '%I:%M%p%a')
            print depart_time, reliability
            return depart_time, reliability
        else:
            print 'Bad flight info'
            return None, None

    def scrape_flight_times(self, depart_time, departure, arrival):
        br = self.br
        supported_airlines = self.supported_airlines
        url = 'http://www.flightstats.com/go/FlightStatus/flightStatusByRoute.do'

        base_url = 'http://www.flightstats.com'

        br.open('http://www.flightstats.com/go/FlightStatus/flightStatusByRoute.do')

        br.select_form('widgetFlightStatusByRouteForm')

        br.form['departure'] = departure
        br.form['arrival'] = arrival

        content = br.submit()

        html = content.read()

        soup = BeautifulSoup(html)

        table = soup.find('table', {'class' : 'flightStatusByAirportListingTable'})
        rows = table.findAll('tr')
        flight_data = []
        for row in rows:
            #remove dud row
            if len(row.findAll('th')) > 0:
                continue
            cols = row.findAll('td')
            flight_url = None
            airline = None
            for col in cols:
                if col.find('a') is not None:
                    #find airline in URL
                    flight_url = base_url + col.find('a')['href']
                    index = flight_url.index('airline=')
                    airline = flight_url[index+8:index+10]
                    break
            #check to see if airline is supported
            if airline not in supported_airlines:
                continue
            flight = [ele.text.strip() for ele in cols]

            #really bad way to remove unwanted elements
            if 'Scheduled' in flight:
                flight.remove('Scheduled')
            if 'On-time' in flight:
                flight.remove('On-time')
            if 'Late' in flight:
                flight.remove('Late')
            if 'En Route' in flight:
                flight.remove('En Route')
            if 'Landed' in flight:
                flight.remove('Landed')
            if 'Delayed' in flight:
                flight.remove('Delayed')

            if flight_url is not None and airline is not None:
                flight.append(flight_url)
                # airline = utils.to_full_name(airline)
                flight.append(airline)
                flight.append(utils.get_url(airline))
            #get rid of empty items and convert form unicode to str
            flight_data.append([str(ele) for ele in flight if len(ele) > 0])
        return flight_data

    def scrape_sort(self, airline, flight_number, departure, arrival):
        depart_time, reliability = self.scrape_flight_info(airline, flight_number)
        flight_data = self.scrape_flight_times(depart_time, departure, arrival)
        results = []

        #build result list
        for flight in flight_data:
            result = flight #each result to be shown on one line of search.html
            depart_time, reliability = self.scrape_flight_info(flight[3])
            #skip flights with unknown ratings
            if reliability is None:
                continue
            result.append(depart_time)
            result.append(reliability)
            results.append(result)

        return sorted(results,key=lambda x: x[6], reverse=True), reliability
