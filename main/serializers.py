from rest_framework import serializers
from .models import HighSchoolPlayer, ProPlayer, Player

class HighSchoolPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighSchoolPlayer
        fields = '__all__'

class ProPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProPlayer
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'