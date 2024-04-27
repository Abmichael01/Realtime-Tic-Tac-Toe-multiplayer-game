from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("lobby", lobby, name="lobby"),
    path("game-room/<str:pk>", game_room, name="game-room"),
    path("create-room", create_room, name="create-room"),
    path("play-game", csrf_exempt(play_game), name="play-game"),
    path("join-room", join_room, name="join-room"),
    path("update-game", csrf_exempt(update_game), name="update-game"),
    path("leaderboard", leaderboard, name="leaderboard"),
]
