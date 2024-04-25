from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import *
from django.http import JsonResponse
import secrets
import string
from django.contrib import messages

# Create your views here.

@login_required
def lobby(request):
    

    return render(request, 'game/lobby.html', {
        "page": "lobby"
    })

def generate_room_code(length=6):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length)).upper()

# Usage


def create_room(request):
    user = request.user
    room_code = generate_room_code()
    while GameRoom.objects.filter(room_code = room_code).exists():
        room_code = generate_room_code()

    print(room_code)
    game_room = GameRoom.objects.create(
        player1 = user,
        room_code = room_code,
    )
    game_room.save()
    game = Game.objects.create(
        game_room = game_room,
        next_player = game_room.player1,
    )
    game.save()
    return redirect("game-room", pk=game_room.id)

def join_room(request):
    if request.method == "POST":
        room_code = request.POST.get("room-code")
        user = request.user
        
        if not GameRoom.objects.filter(room_code=room_code).exists():
            messages.error(request, "Room does not exist")
            return redirect("join-room")
    
        game_room = GameRoom.objects.get(room_code=room_code)
        game_room.player2 = user
        game_room.save()
            

        return redirect("game-room", pk=game_room.id)
    return render(request, "game/join-room.html", {
        "page": "join-room",
    })

def game_room(request, pk):
    room = GameRoom.objects.get(id=pk)

    return render(request, "game/game_room.html", {
        "room": room
    })

def play_game(request):
    if request.method == "POST":
        room_id = request.POST.get("id")
        box = request.POST.get("box")
        print(room_id + "" + box)
        game_room = GameRoom.objects.get(id=room_id)
        game = Game.objects.get(game_room=game_room)

        if box == "1":
            if game.next_player == game_room.player1:
                game.box1 = "X"
                game.next_player = game_room.player2
            else:
                game.box1 = "O"
                game.next_player = game_room.player1
        elif box == "2":
            if game.next_player == game_room.player1:
                game.box2 = "X"
                game.next_player = game_room.player2
            else:
                game.box2 = "O"
                game.next_player = game_room.player1
        elif box == "3":
            if game.next_player == game_room.player1:
                game.box3 = "X"
                game.next_player = game_room.player2
            else:
                game.box3 = "O"
                game.next_player = game_room.player1
        elif box == "4":
            if game.next_player == game_room.player1:
                game.box4 = "X"
                game.next_player = game_room.player2
            else:
                game.box4 = "O"
                game.next_player = game_room.player1
        elif box == "5":
            if game.next_player == game_room.player1:
                game.box5 = "X"
                game.next_player = game_room.player2
            else:
                game.box5 = "O"
                game.next_player = game_room.player1
        elif box == "6":
            if game.next_player == game_room.player1:
                game.box6 = "X"
                game.next_player = game_room.player2
            else:
                game.box6 = "O"
                game.next_player = game_room.player1
        elif box == "7":
            if game.next_player == game_room.player1:
                game.box7 = "X"
                game.next_player = game_room.player2
            else:
                game.box7 = "O"
                game.next_player = game_room.player1
        elif box == "8":
            if game.next_player == game_room.player1:
                game.box8 = "X"
                game.next_player = game_room.player2
            else:
                game.box8 = "O"
                game.next_player = game_room.player1
        elif box == "9":
            if game.next_player == game_room.player1:
                game.box9 = "X"
                game.next_player = game_room.player2
            else:
                game.box9 = "O"
                game.next_player = game_room.player1
        game.save()


        if game.next_player == request.user:
            next_player = True
            return JsonResponse({
                "message": "it's your turn",
                "next_player": next_player,
            })
        
        if game.next_player != request.user:
            next_player = False
            return JsonResponse({
                "message": f"it's {str(game.next_player)}'s turn",
                "next_player": next_player,
            })

        
        

def update_game(request):
    if request.method == "POST":
        room_id = request.POST.get("id")
        game_room = GameRoom.objects.get(id=room_id)
        game = Game.objects.get(game_room=game_room)

        if game_room.player2 == None:
            return JsonResponse({
                "message": "waiting for player 2",
                "waiting": True
            })

        if game.box1 == None:
            box1 = ""
        else:
            box1 = game.box1

        if game.box2 == None:
            box2 = ""
        else:
            box2 = game.box2

        if game.box3 == None:
            box3 = ""
        else:
            box3 = game.box3

        if game.box4 == None:
            box4 = ""
        else:
            box4 = game.box4

        if game.box5 == None:
            box5 = ""
        else:
            box5 = game.box5
        
        if game.box6 == None:
            box6 = ""
        else:
            box6 = game.box6

        if game.box7 == None:
            box7 = ""
        else:
            box7 = game.box7

        if game.box8 == None:
            box8 = ""
        else:
            box8 = game.box8

        if game.box9 == None:
            box9 = ""
        else:
            box9 = game.box9    


        if game.next_player == request.user:
            next_player = True
            return JsonResponse({
                "started": True,
                "message": "it's your turn",
                "next_player": next_player,
                "box1": box1,
                "box2": box2,
                "box3": box3,
                "box4": box4,
                "box5": box5,
                "box6": box6,
                "box7": box7,
                "box8": box8,
                "box9": box9,
                "player2": str(game_room.player2),
            })
        

        if game.next_player != request.user:
            next_player = False
            return JsonResponse({
                "started": True,
                "message": f"it's {str(game.next_player)}'s turn",
                "next_player": next_player,
                "box1": box1,
                "box2": box2,
                "box3": box3,
                "box4": box4,
                "box5": box5,
                "box6": box6,
                "box7": box7,
                "box8": box8,
                "box9": box9,
                "player2": str(game_room.player2),
            })


