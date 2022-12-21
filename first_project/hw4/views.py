from django.shortcuts import render
from django.http import HttpResponse
import pymysql


def main(request):
    choice_list = {'choice_list': [('writers/', 'Writers'), ('books/', 'Top of Books')]}

    return render(request, 'index4.html', context=choice_list)


def writers(request):
    writers = {'choice_list': [('', 'Main'), ('books/', 'Top of Books')],
               'writers': {'s_fitzgerald': "Scott Fitzgerald", 'm_proust': 'Marcel Proust'},
               'writers_all': 'Writers: '}

    return render(request, 'index4.html', context=writers)


def book_top(request):
    top_best_books = {'choice_list': [('', 'Main'), ('writers/', 'Writers')], 'top_books': {'writer1': 'text1',
                                                                                            'writer2': 'text2'}}
    return render(request, 'index4.html', context=top_best_books)
