from django.shortcuts import render
from django.http import HttpResponse
import pymysql


def index(request):
    return HttpResponse("Nothing")


def main(request, name):
    return HttpResponse(f"Hello {name}")


def check(request, number):
    if number % 2 == 0:
        return HttpResponse(f"{number} is even")
    else:
        return HttpResponse(f"{number} is odd")


def connect(request, name, password):
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
        a = ""
        try:
            with connection.cursor() as cursor:
                insert = f"INSERT INTO `students` (name, password) VALUES('{name}', '{password}');"
                cursor.execute(insert)
                connection.commit()
                print("Inserted")
            with connection.cursor() as cursor:
                select_table = f"SELECT * FROM `students`;"
                cursor.execute(select_table)
                result = cursor.fetchall()
                for i in result:
                    a += f"{i}\n"
        finally:
            connection.close()

    except:
        return HttpResponse("Error with connection")

    return HttpResponse(a)


def email_resp(request, email):
    return HttpResponse(f"Your email - {email}")


def phone_resp(request, phone):
    return HttpResponse(f"Your phone - {phone}")
