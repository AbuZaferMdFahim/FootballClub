from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.conf import settings
from django.conf.urls.static import static
#UI
from django.urls import path


urlpatterns = [
    path('',views.home,name='home'),
    path('fixture/',views.fixture,name='fixture'),
    path('player/',views.player,name='player'),
    path('news/',views.news,name='news'),
    path('player_detail/<int:pk>/', views.player_detail, name='player_detail'),
    path('news_detail/<int:pk>/', views.news_detail, name='news_detail'),
    path('contact/', views.contact, name='contact'),
    path('contact_success/', TemplateView.as_view(template_name='contact_success.html'), name='contact_success'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
