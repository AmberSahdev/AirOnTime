from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime

from .forms import SearchForm

from . import utils

def index(request):
    if request.method == 'POST':
        airline = request.POST['airline'].upper()
        departure = request.POST['departure'].upper()
        arrival = request.POST['arrival'].upper()
        flight_id = request.POST['flight']

        return HttpResponseRedirect('/search/?flight={0}&departure={1}&arrival={2}&airline={3}'.format(flight_id,departure,arrival,airline))

    return render(request, 'flights/index.html')


def search(request):
    if 'flight' in request.GET:
        flight_id = request.GET.get('flight').strip().upper()
        departure = request.GET.get('departure').strip().upper()
        arrival = request.GET.get('arrival').strip().upper()
        airline = request.GET.get('airline').strip().replace('/','').upper()
        rating, results = utils.get_search_info(airline, flight_id, departure, arrival)
        if rating is None:
            messages.add_message(request, messages.ERROR, 'Invalid flight information')
            return HttpResponseRedirect('/')
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
    else:
        return HttpResponseRedirect('/')
