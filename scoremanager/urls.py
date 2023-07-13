"""
URL configuration for scoremanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from rest_framework import routers
from backend import views
from backend.views import PlayerListCreateView, PlayerRetrieveUpdateDestroyView
from backend.views import TeamListCreateView, TeamRetrieveUpdateDestroyView
from backend.views import GameListCreateView, GameRetrieveUpdateDestroyView
from backend.views import TeamScoreListCreateView, TeamScoreRetrieveUpdateDestroyView
from backend.views import IndividualScoreListCreateView, IndividualScoreRetrieveUpdateDestroyView


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/players/', PlayerListCreateView.as_view(), name='player-list'),
    path('api/players/<int:pk>/', PlayerRetrieveUpdateDestroyView.as_view(), name='player-detail'),
    path('api/teams/', TeamListCreateView.as_view(), name='team-list'),
    path('api/teams/<int:pk>/', TeamRetrieveUpdateDestroyView.as_view(), name='team-detail'),
    path('api/games/', GameListCreateView.as_view(), name='game-list'),
    path('api/games/<int:pk>/', GameRetrieveUpdateDestroyView.as_view(), name='game-detail'),
    path('api/team-scores/', TeamScoreListCreateView.as_view(), name='team-score-list'),
    path('api/team-scores/<int:pk>/', TeamScoreRetrieveUpdateDestroyView.as_view(), name='team-score-detail'),
    path('api/individual-scores/', IndividualScoreListCreateView.as_view(), name='individual-score-list'),
    path('api/individual-scores/<int:pk>/', IndividualScoreRetrieveUpdateDestroyView.as_view(), name='individual-score-detail'),
]
