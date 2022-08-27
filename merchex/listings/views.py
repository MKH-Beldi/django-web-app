from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect

from listings.models import *
from listings.forms import ContactsUSForm

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
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    if request.method == 'POST':
        form = ContactsUSForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('contact')
    else:
        form = ContactsUSForm()
    return render(request,
                  'listings/contact_us.html',
                  context={'form': form}
                  )