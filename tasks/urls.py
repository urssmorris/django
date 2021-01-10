from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    #path("add1", views.add1, name="add1"),
    #path("add2", views.add1, name="add2")


]
