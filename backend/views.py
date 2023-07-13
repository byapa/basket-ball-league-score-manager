#from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from .models import Team, Player
from backend.serializers import UserSerializer, GroupSerializer, TeamSerializer, PlayerSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlayerListCreateView(generics.ListCreateAPIView):
    """
    API endpoint that allows players to be viewed or created.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows players to be viewed,updated or deleted individually.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TeamListCreateView(generics.ListCreateAPIView):
    """
    API endpoint that allows teams to be viewed or created.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows teams to be viewed,updated or deleted individually.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer