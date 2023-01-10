from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
import datetime
import pymysql
from uploaderjson.models import *
import json


def upload_data_json(request):
    with open('products.json') as file:
        reader = json.load(file)
        for row in reader:
            print(row)
            try:
                _, created = Product.objects.get_or_create(
                    MatchNumber=row['MatchNumber'],
                    RoundNumber=row['RoundNumber'],
                    DateUtc=row['DateUtc'],
                    Location=row['Location'],
                    HomeTeam=row['HomeTeam'],
                    AwayTeam=row['AwayTeam'],
                    Group=row['Group'],
                    HomeTeamScore=row['HomeTeamScore'],
                    AwayTeamScore=row['AwayTeamScore'],
                    )
            except Exception as ex:
                print(ex)
                pass
    return HttpResponse("Done!")