from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game

@login_required(login_url="/users/login/")
def game_list_view(request):
    games = Game.objects.filter(state="ACTIVE")
    return render(request, 'games/list.html', {'games': games})


@login_required(login_url="/users/login/")
def game_new_view(request):

    if request.method == "POST":
        room_name = request.POST.get("room_name")

        if Game.objects.filter(room_name=room_name).exists():
            return render(request, "games/name.html", {
                "error": "Ese nombre ya está en uso."
            })

        new_game = Game.objects.create(
            owner=request.user,
            room_name=room_name,
            player1=request.user,
            board="_________",
            active_player=1,
            state="ACTIVE"
        )

        return redirect('game_detail', game_id=new_game.id)

    return render(request, 'games/name.html')


@login_required(login_url="/users/login/")
def game_detail_view(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    # Puede entrar si es jugador1, jugador2 o si player2 sigue libre
    if request.user in [game.player1, game.player2] or game.player2 is None:
        return render(request, 'games/detail.html', {'game': game})

    return redirect('games_list')


@login_required(login_url="/users/login/")
def game_delete_view(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    if request.user != game.player1:
        return redirect('games_list')

    game.delete()
    return redirect('games_list')


@login_required(login_url="/users/login/")
def game_join_view(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    if game.player2 is None and request.user != game.player1:
        game.player2 = request.user
        game.save()

    return redirect('game_detail', game_id=game.id)
