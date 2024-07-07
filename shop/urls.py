from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('jersey/',views.jersey,name='jersey'),
    path('footballaccesories/',views.footballaccesories,name='footballaccesories'),
    path('turf/',views.turf,name='turf'),
]