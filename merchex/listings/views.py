from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request: HttpRequest):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')
def listings(request):
    return HttpResponse('<h1>List of announcements for articles</h1>')

def contact(request):
    return HttpResponse('<h1>Contact US</h1>')