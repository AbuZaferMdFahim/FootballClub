from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('fixture/',views.fixture,name='fixture'),
    path('player/',views.player,name='player'),
    path('news/',views.news,name='news'),
    path('player_detail/<int:pk>/', views.player_detail, name='player_detail'),
    path('news_detail/<int:pk>/', views.news_detail, name='news_detail'),
]
