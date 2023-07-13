from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Player, Team, Game, IndividualScore, TeamScore


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many = True, read_only = True)
    class Meta:
        model = Team
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'