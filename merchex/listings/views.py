from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render

from listings.models import *

def hello(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/hello.html',
                  context={'bands': bands}
                  )
def listings(request):
    listings = Listings.objects.all()
    return render(request,
                  'listings/listings.html',
                  context={'listings': listings}
                  )

def about(request: HttpRequest):
    return render(request,
                  'listings/about_us.html',
                  )

def contact(request):
    return render(request,
                  'listings/contact_us.html',
                  )