from django.urls import path
from . import views, models

urlpatterns = [
    path("", views.index, name="index"),
<<<<<<< HEAD
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book")
=======
    path("<int:flight_id>", views.flight, name="flight")

>>>>>>> 926755a91b13312731e3573d7d9f9268ff35cc82
]
