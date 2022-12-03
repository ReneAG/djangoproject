from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello Word")

def about(request):
    return HttpResponse("About")