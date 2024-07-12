from django.shortcuts import render
from django.core.paginator import Paginator
from . models import Jersey,FootballAccessory,Turf

# Create your views here.

def shop(request):
    return render(request,'shop.html')

def jersey(request):
    jersey = Jersey.objects.all()
    
    # Pagination
    paginator = Paginator(jersey, 9)  # Show 9 jerseys per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    data = {
        'page_obj': page_obj,
    }
    return render(request, 'jersey.html', data)

def footballaccesories(request):
    footballAccessorys = FootballAccessory.objects.all()
    
    # Pagination
    paginator = Paginator(footballAccessorys, 9)  # Show 9 jerseys per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    data = {
        'page_obj': page_obj,
    }
    return render(request, 'accesories.html',data)

def turf(request):
    turfs = Turf.objects.all()

    # Pagination
    paginator = Paginator(turfs, 9)  # Show 9 jerseys per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    data = {
        'page_obj': page_obj,
    }
    return render(request, 'turf.html',data)