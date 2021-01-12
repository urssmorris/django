from django.contrib import admin

#airlines models
from .models import Flight, Airport, Passenger

#Customizae admin interface(new class)
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

# Register your models here.
#admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Passenger)
admin.site.register(Flight, FlightAdmin)