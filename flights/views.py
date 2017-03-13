from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime

from .forms import SearchForm

import utils

def index(request):
    if request.method == 'POST':
        airline = request.POST['airline'].upper()
        departure = request.POST['departure'].upper()
        arrival = request.POST['arrival'].upper()
        flight_id = request.POST['flight']

        return search(request, flight_id, departure, arrival, airline)

    return render(request, 'flights/index.html')

def search(request, flight_id, departure, arrival, airline):
    rating, results = utils.get_search_info(airline, flight_id, departure)
    if rating is None:
        messages.add_message(request, messages.ERROR, 'Invalid flight information')
        index(request)
    airline = utils.to_full_name(airline)
    context = {
        'flight_id': flight_id,
        'departure': departure,
        'arrival': arrival,
        'airline': airline,
        'rating': rating,
        'results': results,
    }
    return render(request, 'flights/search.html', context)
