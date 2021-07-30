#import django
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    return HttpResponse("Welcome the the Meeting Planner")

def date(request):
    return HttpResponse("Welcome the the Meeting Planner " + str(datetime.now()) )

def about(request):
    return HttpResponse("I am <b>Huy Pham</b>")