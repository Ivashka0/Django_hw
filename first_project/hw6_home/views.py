from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
import datetime
import pymysql


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
