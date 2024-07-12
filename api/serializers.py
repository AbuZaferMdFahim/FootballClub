from rest_framework import serializers
from club.models import Fixture,Player,News
from shop.models import Jersey, FootballAccessory, Turf

class FixtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixture
        fields = '__all__'
        
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
        
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class JerseySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jersey
        fields = '__all__'

class FootballAccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballAccessory
        fields = '__all__'

class TurfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turf
        fields = '__all__'
