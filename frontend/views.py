from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Home Page')

def about(request):
    return HttpResponse('About Us Page')


def services(request):
    return HttpResponse('<h1>Services</h1>')

def contact(request):
    return HttpResponse('<h1>Contact Us</h1>')
