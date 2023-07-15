from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Aliens are here!; AI is here!; Robots are here!;')
