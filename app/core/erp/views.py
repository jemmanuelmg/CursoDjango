from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def myfirstview(request):
    return HttpResponse('hola esta es mi primera url')