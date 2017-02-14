from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from itertools import chain
import random
from dal import autocomplete
from search.models import *
from Bomztrip.forms import SearchForm


def home(request):
    return render(request, 'home.html', {'form': SearchForm(initial={'keyword': 'Europe'})})

def trips(request):
    return render(request, 'trips.html', {'trips': Trip.objects.order_by('-likes')})

def random_trip(request):
    keyword = request.POST.get('keyword')
    checks = request.POST.getlist("checkbox_custom")
    print checks
    trips_city = Trip.objects.filter(city__icontains= keyword)
    trips_country = (Trip.objects.filter(country__icontains = keyword))
    trips_continent = (Trip.objects.filter(continent__icontains = keyword))
    trips = list(chain(trips_city, trips_country, trips_continent))
    random_trip = trips[random.randint(0, len(trips)-1)]
    image_list = random_trip.images.all()
    return render(request, 'trip.html', {'trip': random_trip, 'pictures': image_list, 'form': SearchForm})

class SearchAutocomplete(autocomplete.Select2ListView):
    def get_list(self):
        cities = [i['city'] for i in Trip.objects.values('city')]
        countries = [i['country'] for i in Trip.objects.values('country')]
        continents = [i['continent'] for i in Trip.objects.values('continent')]
        total = cities + countries + continents
        final = []
        [final.append(item) for item in total if item not in final]
        return final


def like(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['trip_id']

    likes = 0
    if cat_id:
        cat = Trip.objects.get(id=int(cat_id))
        if cat:
            likes = cat.likes + 1
            cat.likes =  likes
            cat.save()
    return HttpResponse(likes)

def affiliates(request):
    return render(request, 'working.html')

def contacts(request):
    return render(request, 'working.html')