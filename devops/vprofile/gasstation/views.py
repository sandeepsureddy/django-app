from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("refill the fuel in the car - gasstation ")
# Create your views here.
