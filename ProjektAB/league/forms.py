from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Imię (opcjonalne).')
    last_name = forms.CharField(max_length=30, required=False, help_text='Nazwisko (opcjonalne).')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    username = forms.CharField(max_length=30, required=False, help_text='Nazwa użytkownika.')
    password1 = forms.CharField(max_length=30, required=False, help_text='Hasło')
    password2 = forms.CharField(max_length=30, required=False, help_text='Potwierdz hasło')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'nick', 'CountryofBirth', 'age', 'current_team', 'player_Img']

class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ['first_name', 'last_name', 'nick', 'coach_Img']

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['winner', 'loser', 'sezon', 'time']

class PentaKillForm(forms.ModelForm):
    class Meta:
        model = PentaKill
        fields = ['player', 'game', 'minute']

class TeamHistoryForm(forms.ModelForm):
    class Meta:
        model = TeamHistory
        fields = ['team', 'player', 'join_date', 'leave_date']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'leagueSezon', 'classification', 'team_logo', 'top', 'jung', 'mid', 'adc', 'supp', 'coach']

class LeagueClassificationForm(forms.ModelForm):
    class Meta:
        model = LeagueClassification
        fields = ['ranking_position']

class SezonForm(forms.ModelForm):
    class Meta:
        model = Sezon
        fields = ['league', 'number', 'begin_date', 'end_date']

class LeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ['name', 'location', 'league_logo']