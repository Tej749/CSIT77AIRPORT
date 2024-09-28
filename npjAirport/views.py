from django.shortcuts import render, redirect
from django.contrib import messages
from . import global_message
from .models import Csit

# Create your views here.

def index(request):
    data = Csit.objects.all()
    return render(request, "npjAirport/index.html", {'data' : data})

def table(request):
    data = Csit.objects.all()
    return render(request, "npjAirport/table.html", {'data' : data})

def form(request):
    if request.method == 'POST':
        det = request.POST
        name = det.get('name')
        add = det.get('add')
        mob = det.get('mob')
        email = det.get('email')
        Csit.objects.create(name=name, add=add, mob=mob, email=email)
        messages.success(request, global_message.SUCCESS_MESSAGE)
        return redirect("/form")

    return render(request, "npjAirport/form.html")

def edit(request, pk):
    if request.method == 'POST':
        det = request.POST
        name = det.get('name')
        add = det.get('add')
        mob = det.get('mob')
        email = det.get('email')
        dm = Csit.objects.get(id=pk)
        dm.name = name
        dm.add = add
        dm.mob = mob
        dm.email = email
        dm.save()
        messages.success(request, "Data Edit Successfully...!")
        return redirect('/')
    dt = Csit.objects.get(id=pk)
    return render(request, "npjAirport/edit.html", {'dt':dt})


def contact(request):
    return render(request, "npjAirport/contact.html")

def delete(request, pk):
    Csit.objects.get(id=pk).delete()
    messages.success(request, global_message.DELETE_MSG)
    return redirect('/')



