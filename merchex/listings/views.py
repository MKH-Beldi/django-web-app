from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render

from listings.models import *

def hello(request):
    bands = Band.objects.all()
    listings = Listings.objects.all()
    return render(request,
                  'listings/hello.html',
                  context={'bands': bands}
                  )

def about(request: HttpRequest):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')
def listings(request):
    return HttpResponse('<h1>List of announcements for articles</h1>')

def contact(request):
    return HttpResponse('<h1>Contact US</h1>')