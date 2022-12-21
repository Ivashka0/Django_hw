from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
import datetime


def dictsort(request):
    context = {"questions": [
        {'id': 2,
         'author': 'oliver',
         'question_text': 'Что первично, дух или материя?',
         'date': datetime.date(year=2006, month=7, day=14)
         },
        {'id': 3,
         'author': 'anthony',
         'question_text': 'Существует ли свобода воли?',
         'date': datetime.date(year=2007, month=7, day=14)},
        {'id': 1,
         'author': 'annie',
         'question_text': '',
         'date': datetime.date(year=2005, month=7, day=14)}
    ]}
    return render(template_name='index5.html', request=request, context=context)


def pri(request):
    lets_do_it = [{'priority': 100, 'task': 'Составить список дел'},
                  {'priority': 150, 'task': 'Изучать Django'},
                  {'priority': 1, 'task': 'Подумать о смысле жизни'}]
    return render(template_name='index5.1.html', request=request, context={"lets_do_it": lets_do_it})


def pra(request):
    lets_do_it = [{'name': 'Шаддам IV', 'surname': 'Коррино'},
                  {'name': 'Пол', 'surname': 'Атрейдес'},
                  {'name': 'Франклин', 'surname': 'Герберт'}]

    return render(template_name='index5.2.html', request=request, context={"lets_do_it": lets_do_it})


def pre(request):
    latest_question_list = [{'id': 1, 'question_text': 'В чем смысл жизни?'},
                            {'id': 2, 'question_text': 'Что первично, дух или материя?'},
                            {'id': 3, 'question_text': ''}]

    return render(template_name='index5.3.html', request=request, context={"latest_question_list": latest_question_list})
