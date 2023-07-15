from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import Game, GamePlayer, GameTeam, Player, Team


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the User model
    """
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Group model
    """
    class Meta:
        model = Group
        fields = ["url", "name"]


class TeamScoreSerializer(serializers.ModelSerializer):
    """
    Serializer for the Team model
    """
    class Meta:
        model = GameTeam
        fields = "__all__"


class GamePlayerSerializer(serializers.ModelSerializer):
    """
    Serializer for the GamePlayer model
    """
    class Meta:
        model = GamePlayer
        fields = "__all__"


class PlayerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Player model
    """
    scores = GamePlayerSerializer(many=True, read_only=True)
    average_score = serializers.SerializerMethodField()

    def get_average_score(self, obj):
        return obj.average_score

    class Meta:
        model = Player
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    """
    Serializer for the Team model
    """
    players = PlayerSerializer(many=True, read_only=True)
    average_score = serializers.SerializerMethodField()

    def get_average_score(self, obj):
        return obj.average_score

    class Meta:
        model = Team
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    """
    Serializer for the Game model
    """
    class Meta:
        model = Game
        fields = "__all__"
