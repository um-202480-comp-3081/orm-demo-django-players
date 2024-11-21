from django.shortcuts import render, get_object_or_404
from .models import Player

# Create your views here.

def player_list(request):
    players = Player.objects.all()
    return render(request, 'players/player_list.html', {'players': players})

def player_detail(request, id):
    player = get_object_or_404(Player, id=id)
    return render(request, 'players/player_detail.html', {'player': player})
