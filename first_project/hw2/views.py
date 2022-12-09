from django.shortcuts import render
from django.http import HttpResponse
import pymysql


def main(request):
    return render(request, 'index.html', context={'text': 'hello world', 'pagelist': [('main', 'Main'), ('news', 'News'), ('management', 'Management'), ('facts', 'Facts'), ('contacts', 'Contacts'), ('history', 'History')]})


main_page = f'<ul><li><a href="http://127.0.0.1:8000">Main</a></li></ul>'
news_page = f'<ul><li><a href="http://127.0.0.1:8000/news">News</a></li></ul>'
management_page = f'<ul><li><a href="http://127.0.0.1:8000/management">Management</a></li></ul>'
contacts_page = f'<ul><li><a href="http://127.0.0.1:8000/contacts">Contacts</a></li></ul>'
facts_page = f'<ul><li><a href="http://127.0.0.1:8000/facts">Facts</a></li></ul>'
history_page = f'<ul><li><a href="http://127.0.0.1:8000/history">Facts</a></li></ul>'


def news(request):
    return HttpResponse(f"{main_page}{management_page}{contacts_page}{facts_page}{history_page}<br>Will be available soon!")


def management(request):
    return HttpResponse(f"{main_page}{news_page}{contacts_page}{facts_page}{history_page}<br>No one!")


def history_total(request):
    return HttpResponse(f"{main_page}{news_page}{management_page}{contacts_page}{facts_page}<br>Choose parameter(photo/people/else)")


def history(request, parameter):
    if parameter == "people":
        return HttpResponse(f"{main_page}{news_page}{management_page}{contacts_page}{facts_page}<br>No famous people")
    elif parameter == "photo":
        return HttpResponse(f"{main_page}{news_page}{management_page}{contacts_page}{facts_page}<br>No photo")
    else:
        return HttpResponse(f"{main_page}{news_page}{management_page}{contacts_page}{facts_page}<br>Nothing haven`t found about {parameter}")


def facts(request):
    return HttpResponse(f"{main_page}{news_page}{management_page}{contacts_page}{history_page}<br>Some facts there")


def contacts(request):
    return HttpResponse(f"{main_page}{news_page}{management_page}{facts_page}{history_page}<br>No contacts there,so you can`t complain anyone.")
