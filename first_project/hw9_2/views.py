from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
import datetime
import pymysql
from hw9_2.models import Product
import os


def product(request):
    context = Product.objects.all()
    return render(template_name='index9_2.html', request=request, context={"products_list": context})
