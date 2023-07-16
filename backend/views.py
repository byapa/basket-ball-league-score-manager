import numpy as np
from django.contrib.auth.models import Group, User
from django.http import JsonResponse
from rest_framework import generics, viewsets

from backend.serializers import (GameSerializer, GroupSerializer,
                                 GamePlayerSerializer, PlayerSerializer,
                                 TeamScoreSerializer, TeamSerializer,
                                 UserSerializer)
from .models import Game, GamePlayer, GameTeam, Player, Team


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]


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


class GameListCreateView(generics.ListCreateAPIView):
    """
    API endpoint that allows games to be viewed or created.
    """

    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows games to be viewed,updated or deleted individually.
    """

    queryset = Game.objects.all()
    serializer_class = GameSerializer


class TeamScoreListCreateView(generics.ListCreateAPIView):
    """
    API endpoint that allows team scores to be viewed or created.
    """

    queryset = GameTeam.objects.all()
    serializer_class = TeamScoreSerializer


class TeamScoreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows team scores to be viewed,updated or deleted individually.
    """

    queryset = GameTeam.objects.all()
    serializer_class = TeamScoreSerializer


class IndividualScoreListCreateView(generics.ListCreateAPIView):
    """
    API endpoint that allows individual scores to be viewed or created.
    """

    queryset = GamePlayer.objects.all()
    serializer_class = GamePlayerSerializer


class IndividualScoreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows individual scores to be viewed,updated or deleted individually.
    """

    queryset = GamePlayer.objects.all()
    serializer_class = GamePlayerSerializer


def top_players_view(_request, team_id):
    """
    API endpoint that allows the retrieval of top players in a team
    """

    all_players = list(Player.objects.filter(team=team_id))

    response_data = []

    if all_players:
        ninetieth_percentile_score = _get_ninetieth_percentile_score(all_players)

        all_players_in_ninetieth_percentile = list(
            filter(
                lambda player: player.average_score > 0
                               and player.average_score >= ninetieth_percentile_score,
                all_players,
            )
        )

        serializer = PlayerSerializer(all_players_in_ninetieth_percentile, many=True)
        response_data = serializer.data

    return JsonResponse(response_data, safe=False)


def _get_ninetieth_percentile_score(players):
    players_sorted_by_avg_score = sorted(
        players, key=lambda player: player.average_score
    )

    sorted_avg_scores = list(
        map(lambda player: player.average_score, players_sorted_by_avg_score)
    )

    return np.percentile(sorted_avg_scores, 90)
