from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    flight_id = request.GET.get('flight').strip().upper()
    departure = request.GET.get('departure').strip().upper()
    arrival = request.GET.get('arrival').strip().upper()
    airline = request.GET.get('airline').strip().replace('/','').upper()
    rating, all_results = utils.get_search_info(airline, flight_id, departure, arrival)
    if rating is None:
        messages.add_message(request, messages.ERROR, 'Invalid flight information')
        return HttpResponseRedirect('/')
    airline_full = utils.to_full_name(airline)


    paginator = Paginator(all_results, 10)
    page = request.GET.get('page')

    try:
        results_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        results_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        results_page = paginator.page(paginator.num_pages)

    print(results_page[0])

    context = {
        'flight_id': flight_id,
        'departure': departure,
        'arrival': arrival,
        'airline_full': airline_full,
        'airline': airline,
        'rating': rating,
        'all_results': results_page
    }
    return render(request, 'flights/search.html', context)


def about(request):
    return render(request, 'flights/about.html')


def contact(request):
    return render(request, 'flights/contact.html')
