from django.shortcuts import render
from django.http import HttpResponse
import pymysql


def main(request):
    return render(request, 'index3.html', context={'text': 'hello world', 'pagelist': [('main', 'Main'), ('facts', 'Facts'), ('cities', 'Cities'), ('history', 'History')]})


main_page = f'<ul><li><a href="http://127.0.0.1:8000">Main</a></li></ul>'
history_page = f'<ul><li><a href="http://127.0.0.1:8000/history">History</a></li></ul>'
cities_page = f'<ul><li><a href="http://127.0.0.1:8000/cities">Cities</a></li></ul>'
facts_page = f'<ul><li><a href="http://127.0.0.1:8000/facts">Facts</a></li></ul>'


def history_total(request):
    return HttpResponse(f"{main_page}{cities_page}{facts_page}<br>Choose date")


def history(request, date):
    if date == 1871:
        return HttpResponse(f"{main_page}{cities_page}{facts_page}<br>Franco-Prussian war,where they lost.")
    elif date == 1914:
        return HttpResponse(f"{main_page}{cities_page}{facts_page}<br>France was drawn in the Great War")
    else:
        return HttpResponse(f"{main_page}{cities_page}{facts_page}<br>Nothing haven`t found about date - {date}")


def facts(request):
    content = "<ul><li>Fact 1</li><li>Fact 2</li><li>Fact 3</li><li>Fact 4</li></ul>"
    return HttpResponse(f"{main_page}{cities_page}{history_page}<br>Some facts:<br>{content}")


def cities(request):
    city_list = "<ul><li>Paris</li><li>Brest</li><li>Lille</li><li>Nant</li></ul>"
    return HttpResponse(f"{main_page}{facts_page}{history_page}<br>Some cities in France:<br>{city_list}")


def city(request, name_city):
    if name_city.lower() == "paris":
        return HttpResponse(f"{main_page}{facts_page}{history_page}<br>Paris is famous for Eiffel Tower")
    elif name_city.lower() == "brest":
        return HttpResponse(f"{main_page}{facts_page}{history_page}<br>Brest is big coast city in the west of France.")
    else:
        return HttpResponse(f"{main_page}{facts_page}{history_page}<br>Nothing haven`t found about city - {name_city}<br>Return to the list of cities:<br>{cities_page}")


def city_data(request, name_city, year):
    if name_city.lower() == "paris" and year == 1812:
        return HttpResponse(f"{main_page}{facts_page}{history_page}<br>Napoleon")
    elif name_city.lower() == "brest" and year == 1940:
        return HttpResponse(f"{main_page}{facts_page}{history_page}<br>There citizens of France were evacuated there in the UK.")
    else:
        return HttpResponse(f"{main_page}{facts_page}{history_page}<br>Nothing haven`t found about city and this year - {name_city} in {year}<br>Return to the list of cities:<br>{cities_page}")
