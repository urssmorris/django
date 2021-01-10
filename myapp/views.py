from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "myapp/index.html")
    #return HttpResponse("<h1 style=\"color:blue\">Hello, world!</h1>")
    #return HttpResponse("Hello, world!")

def brian(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name):
    return render(request, "hello/geet.html",
    {"name": name.capitalize()})
    #return HttpResponse(f"Hello, {name.capitalize()}!")