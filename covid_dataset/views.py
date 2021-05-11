from django.shortcuts import render
from .models import *
# методы которые будут вызваны при переходе пользователя на какую-либо страницу.

def index(request):
    posts = CountryWiseLatest.objects.all()
    return render(request, 'covid_dataset/index.html', {'posts': posts, 'title': 'COVID-19 stats'})

def map(request):
    data = {'title': 'COVID-19 map'}
    return render(request, 'covid_dataset/map.html', data)

def rus_stat(request):
    data = {'title': 'COVID-19 in Russia'}
    return render(request, 'covid_dataset/Russian_stat', data)

def vac(request):
    data = {'title': 'World vaccinations stats'}
    return render(request, 'covid_dataset/World_vaccinations', data)
