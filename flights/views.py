from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime

from .forms import SearchForm

from scrape import Scraper
import utils

def index(request):
    if request.method == 'POST':
        airline = request.POST['airline'].upper()
        departure = request.POST['departure'].upper()
        arrival = request.POST['arrival'].upper()
        flight_id = request.POST['flight']

        scraper = Scraper()
        depart_time, reliability = scraper.scrape_flight_info(airline, flight_id)

        if reliability is not None:
            return HttpResponseRedirect('/search/flight={0}&departure={1}&arrival={2}&airline={3}'.format(flight_id, departure, arrival, airline))

        messages.add_message(request, messages.ERROR, 'Invalid flight information')


    return render(request, 'flights/index.html')

def search(request, flight_id, departure, arrival, airline):
    scraper = Scraper()
    results, reliability = scraper.scrape_sort(airline, flight_id, departure, arrival)
    airline = utils.to_full_name(airline)
    print airline
    context = {
        'flight_id': flight_id,
        'departure': departure,
        'arrival': arrival,
        'airline': airline,
        'reliability': reliability,
        'results': results,
    }
    return render(request, 'flights/search.html', context)
