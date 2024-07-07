
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from . models import Jersey,FootballAccessory,Turf
# Create your views here.

def shop(request):
    return render(request,'shop.html')

def jersey(request):
    jerseys = Jersey.objects.all()
    data = {
        "jerseys":jerseys
    }
    return render(request, 'jersey.html',data)

def footballaccesories(request):
    footballAccessorys = FootballAccessory.objects.all()
    data = {
        "footballAccessorys":footballAccessorys
    }
    return render(request, 'accesories.html',data)

def turf(request):
    turfs = Turf.objects.all()
    data = {
        "turfs":turfs
    }
    return render(request, 'turf.html',data)