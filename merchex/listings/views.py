from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render

from listings.models import *

def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  context={'bands': bands}
                  )

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  context={'band': band}
                  )
def listing_list(request):
    listings = Listings.objects.all()
    return render(request,
                  'listings/listings_list.html',
                  context={'listings': listings}
                  )

def listing_detail(request, id):
    listing = Listings.objects.get(id=id)
    return render(request,
                  'listings/listings_detail.html',
                  context={'listing': listing}
                  )
def about(request: HttpRequest):
    return render(request,
                  'listings/about_us.html',
                  )

def contact(request):
    return render(request,
                  'listings/contact_us.html',
                  )