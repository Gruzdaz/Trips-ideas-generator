from django.contrib import admin
from search.models import *

class TripImageInline(admin.TabularInline):
    model = TripImage

class TripAdmin(admin.ModelAdmin):
    inlines = [ TripImageInline, ]

class TripImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Trip, TripAdmin)
admin.site.register(TripImage, TripImageAdmin)