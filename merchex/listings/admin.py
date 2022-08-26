from django.contrib import admin
from listings.models import Band
from listings.models import Listings

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'year_formed')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band')

admin.site.register(Band, BandAdmin)
admin.site.register(Listings, ListingAdmin)