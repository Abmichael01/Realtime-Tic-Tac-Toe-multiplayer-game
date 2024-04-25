from django.db import models
from django.contrib.auth.models import User
import uuid

class GameRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    player1 = models.ForeignKey(User, related_name="player1", on_delete = models.CASCADE)
    player2 = models.ForeignKey(User, related_name="player2", on_delete = models.CASCADE, null=True)
    winner = models.ForeignKey(User, related_name="winner", on_delete = models.CASCADE, null=True)
    room_code = models.CharField(max_length=6, null=True)

class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game_room = models.ForeignKey(GameRoom, related_name="game_room", on_delete = models.CASCADE)
    next_player = models.ForeignKey(User, related_name="next_player", on_delete = models.CASCADE, null=True)
    box1 = models.CharField(max_length=1, null=True)
    box2 = models.CharField(max_length=1, null=True)
    box3 = models.CharField(max_length=1, null=True)
    box4 = models.CharField(max_length=1, null=True)
    box5 = models.CharField(max_length=1, null=True)
    box6 = models.CharField(max_length=1, null=True)
    box7 = models.CharField(max_length=1, null=True)
    box8 = models.CharField(max_length=1, null=True)
    box9 = models.CharField(max_length=1, null=True)




