from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
import datetime
import pymysql
from hw7.models import Product, Departments, Diseases, Doctors, Examinations, Wards


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

    return render(template_name='index7.html', request=request, context={"product_list": context})


def wards_all(request):
    context = Wards.objects.all()

    return render(template_name='index7.html', request=request, context={"wards_list": context})


def departments_all(request):
    context = Departments.objects.all()

    return render(template_name='index7.html', request=request, context={"departments_list": context})


def examinations_all(request):
    context = Examinations.objects.all()

    return render(template_name='index7.html', request=request, context={"examinations_list": context})


def doctors_all(request):
    context = Doctors.objects.all()

    return render(template_name='index7.html', request=request, context={"doctors_list": context})


def diseases_all(request):
    context = Diseases.objects.all()

    return render(template_name='index7.html', request=request, context={"diseases_list": context})
