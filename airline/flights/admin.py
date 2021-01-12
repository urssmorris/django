from django.contrib import admin

#airlines models
<<<<<<< HEAD
from .models import Flight, Airport, Passenger

#Customizae admin interface(new class)
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

# Register your models here.
#admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Passenger)
admin.site.register(Flight, FlightAdmin)
=======
from .models import Flight, Airport

# Register your models here.
admin.site.register(Flight)
admin.site.register(Airport)
>>>>>>> 926755a91b13312731e3573d7d9f9268ff35cc82
