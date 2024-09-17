from django.shortcuts import render
from .models import Csit

# Create your views here.

def index(request):
    data = Csit.objects.all()
    return render(request, "npjAirport/index.html", {'data' : data})

def form(request):
    return render(request, "npjAirport/form.html")

def about(request):
    return render(request, "npjAirport/about.html")

def contact(request):
    return render(request, "npjAirport/contact.html")



