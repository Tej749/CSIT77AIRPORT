from django.shortcuts import render
from .models import Csit

# Create your views here.

def index(request):
    data = Csit.objects.all()
    return render(request, "npjAirport/index.html", {'data' : data})
