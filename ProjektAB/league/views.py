from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db.models import Q

from .forms import *

from .models import PentaKill, Player, Game, League, Coach, TeamHistory, Team, Sezon


def index(request):
    league_list = League.objects.all
    context = {'league_list': league_list}
    return render(request, 'league/index.html', context)

def league_sezons(request, league_id):
    league = get_object_or_404(League, pk=league_id)
    return render(request, 'league/league_sezons.html', {'league': league})

def sezon_teams(request, sezon_id):
    sezon = get_object_or_404(Sezon, pk=sezon_id)
    game_list = Game.objects.filter(sezon=sezon_id)
    player_list = Player.objects.all
    teams = Team.objects.all().order_by('classification')
    return render(request, 'league/sezon_teams.html', {'sezon': sezon, 'game_list': game_list, 'player_list': player_list, 'teams': teams})

def team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    game_list = Game.objects.filter(Q(winner=team_id) | Q(loser=team_id))
    return render(request, 'league/team.html', {'team': team, 'game_list': game_list})

def player(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    team_list = Team.objects.all
    penta_list = PentaKill.objects.filter(player = player_id).all
    history_list = TeamHistory.objects.filter(player = player_id).all
    return render(request, 'league/player.html', {'player': player, 'team_list': team_list, 'penta_list': penta_list, 'history_list': history_list})

def coach(request, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id)
    team_list = Team.objects.all
    return render(request, 'league/coach.html', {'coach': coach, 'team_list': team_list})

def signup(request):
    template_name = 'registration/signup.html'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, template_name, {'form': form})


def player_upload_view(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlayerForm()
    return render(request, 'league/player_upload.html', {'form': form})

def player_update_view(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    form = PlayerForm(request.POST or None, request.FILES or None, instance=player)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'league/player_update.html', {'form': form})

def player_delete_view(request, player_id):
    player = get_object_or_404(Player, pk=player_id)

    if request.method == 'POST':
        player.delete()
        return redirect('home')

    return render(request, 'league/player_delete.html', {'player': player})


def coach_upload_view(request):
    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CoachForm()
    return render(request, 'league/coach_upload.html', {'form': form})

def coach_update_view(request, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id)
    form = CoachForm(request.POST or None, request.FILES or None, instance=coach)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'league/coach_update.html', {'form': form})

def coach_delete_view(request, coach_id):
    coach = get_object_or_404(Player, pk=coach_id)

    if request.method == 'POST':
        coach.delete()
        return redirect('home')

    return render(request, 'league/coach_delete.html', {'coach': coach})

def team_upload_view(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeamForm()
    return render(request, 'league/team_upload.html', {'form': form})

def team_update_view(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    form = TeamForm(request.POST or None, request.FILES or None, instance=team)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'league/team_update.html', {'form': form})

def team_delete_view(request, team_id):
    team = get_object_or_404(Team, pk=team_id)

    if request.method == 'POST':
        team.delete()
        return redirect('home')

    return render(request, 'league/team_delete.html', {'team': team})

def game_upload_view(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GameForm()
    return render(request, 'league/game_upload.html', {'form': form})

def game_update_view(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    form = GameForm(request.POST or None, request.FILES or None, instance=game)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'league/game_update.html', {'form': form})

def game_delete_view(request, game_id):
    game = get_object_or_404(Game, pk=game_id)

    if request.method == 'POST':
        game.delete()
        return redirect('home')

    return render(request, 'league/game_delete.html', {'game': game})

def teamHistory_upload_view(request):
    if request.method == 'POST':
        form = TeamHistoryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeamHistoryForm()
    return render(request, 'league/teamhistory_upload.html', {'form': form})

def pentakill_upload_view(request):
    if request.method == 'POST':
        form = PentaKillForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PentaKillForm()
    return render(request, 'league/pentakill_upload.html', {'form': form})

def sezon_upload_view(request):
    if request.method == 'POST':
        form = SezonForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SezonForm()
    return render(request, 'league/sezon_upload.html', {'form': form})

def sezon_update_view(request, sezon_id):
    sezon = get_object_or_404(Sezon, pk=sezon_id)
    form = SezonForm(request.POST or None, request.FILES or None, instance=sezon)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'league/sezon_update.html', {'form': form})

def sezon_delete_view(request, sezon_id):
    sezon = get_object_or_404(Sezon, pk=sezon_id)

    if request.method == 'POST':
        sezon.delete()
        return redirect('home')

    return render(request, 'league/sezon_delete.html', {'sezon': sezon})

def league_upload_view(request):
    if request.method == 'POST':
        form = LeagueForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LeagueForm()
    return render(request, 'league/league_upload.html', {'form': form})

def league_update_view(request, league_id):
    league = get_object_or_404(League, pk=league_id)
    form = LeagueForm(request.POST or None, request.FILES or None, instance=league)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'league/league_update.html', {'form': form})

def league_delete_view(request, league_id):
    league = get_object_or_404(League, pk=league_id)

    if request.method == 'POST':
        league.delete()
        return redirect('home')

    return render(request, 'league/league_delete.html', {'league': league})