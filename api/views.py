from rest_framework import viewsets,permissions
from club.models import Fixture, Player, News
from shop.models import Jersey, FootballAccessory,Turf
from .serializers import FixtureSerializer, PlayerSerializer, NewsSerializer, JerseySerializer, TurfSerializer, FootballAccessorySerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.
class SuperuserOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser
    
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class FixtureViewSet(viewsets.ModelViewSet):
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer
    permission_classes = [SuperuserOnlyPermission]    
    
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [SuperuserOnlyPermission]

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [SuperuserOnlyPermission]
    
class JerseyViewSet(viewsets.ModelViewSet):
    queryset = Jersey.objects.all()
    serializer_class = JerseySerializer
    permission_classes = [SuperuserOnlyPermission]
    
class FootballAccessoryViewSet(viewsets.ModelViewSet):
    queryset = FootballAccessory.objects.all()
    serializer_class = FootballAccessorySerializer
    permission_classes = [SuperuserOnlyPermission]
    
class TurfViewSet(viewsets.ModelViewSet):
    queryset = Turf.objects.all()
    serializer_class = TurfSerializer
    permission_classes = [SuperuserOnlyPermission]

