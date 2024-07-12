from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FixtureViewSet,PlayerViewSet,NewsViewSet,JerseyViewSet,TurfViewSet,FootballAccessoryViewSet
from .views import CustomAuthToken

router = DefaultRouter()
router.register(r'fixtures', FixtureViewSet),
router.register(r'players',PlayerViewSet),
router.register(r'news',NewsViewSet),
router.register(r'jerseys',JerseyViewSet),
router.register(r'footballaccesories',FootballAccessoryViewSet),
router.register(r'turfs',TurfViewSet),

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomAuthToken.as_view(), name='api-login'),
]
