from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
import datetime
import pymysql
from hw11.models import *


def connect(request):
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="22032007Ivan",
            database="test_python",
            cursorclass=pymysql.cursors.DictCursor
        )
        print("ok")
        try:
            with connection.cursor() as cursor:
                select_table = f"SELECT * FROM `phones_shop`;"
                cursor.execute(select_table)
                result = cursor.fetchall()
        finally:
            connection.close()

    except:
        return HttpResponse("Error with connection")

    return render(template_name='index6_home.html', request=request, context={"result": result})


def product(request):
    context = Product.objects.all()
    categories = Categories.objects.all()

    return render(template_name='index11.html', request=request,
                  context={"products_list": context, "categories_list": categories})


def products_filter(request, category):
    context = Product.objects.filter(style__name=category)
    categories = Categories.objects.all()

    return render(template_name='index11.html', request=request,
                  context={"products_list": context, "categories_list": categories})


def sort_cheapest(request):
    cheapest_products = Product.objects.all().order_by('price')

    return render(template_name='index11.html', request=request, context={"products_list": cheapest_products})


def sort_expensive(request):
    expensive_products = Product.objects.all().order_by('-price')

    return render(template_name='index11.html', request=request, context={"products_list": expensive_products})
