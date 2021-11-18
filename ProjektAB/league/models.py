from django.db import models

class League(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    league_logo = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name

class Sezon(models.Model):
    number = models.CharField(max_length=200)
    begin_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    league = models.ForeignKey(League, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.league.name + ": " + str(self.number)

class LeagueClassification(models.Model):
    ranking_position = models.IntegerField(default=1)
    def __str__(self):
        return "Ranking: " + str(self.ranking_position)

class Player(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nick = models.CharField(max_length=200)
    CountryofBirth = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    current_team = models.ForeignKey('Team', null=True, blank=True, on_delete=models.SET_NULL, related_name='current_team')
    player_Img = models.ImageField(null=True, blank=True)
    def __str__(self):
        return "gracz: " + self.first_name + " \"" + self.nick + "\" " + self.last_name

class Coach(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nick = models.CharField(max_length=200)
    coach_Img = models.ImageField(null=True, blank=True)
    def __str__(self):
        return "Trener: " + self.first_name + " \"" + self.nick + "\" " + self.last_name

class Team(models.Model):
    classification = models.ForeignKey(LeagueClassification, null=True, blank=True, on_delete=models.SET_NULL)
    leagueSezon = models.ForeignKey(Sezon, null=True, on_delete=models.SET_NULL)
    top = models.ForeignKey(Player, null=True, blank=True, on_delete=models.SET_NULL, related_name='top')
    jung = models.ForeignKey(Player, null=True, blank=True, on_delete=models.SET_NULL, related_name='jung')
    mid = models.ForeignKey(Player, null=True, blank=True, on_delete=models.SET_NULL, related_name='mid')
    adc = models.ForeignKey(Player, null=True, blank=True, on_delete=models.SET_NULL, related_name='adc')
    supp = models.ForeignKey(Player, null=True, blank=True, on_delete=models.SET_NULL, related_name='supp')
    coach = models.ManyToManyField(Coach, blank=True)
    name = models.CharField(max_length=200)
    team_logo = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name + " (" + self.leagueSezon.number + ")"

class TeamHistory(models.Model):
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    player = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)
    join_date = models.DateField('data rozpoczecia wspolpracy')
    leave_date = models.DateField('data zakonczenia wspolpracy')
    def __str__(self):
        return "Historia: " + self.team.name + " " + self.player.nick
    def get_join_date(self):
        return str(self.join_date)
    def get_leave_date(self):
        return str(self.leave_date)

class Game(models.Model):
    winner = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name='winnerteam')
    loser = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name='loserteam')
    sezon = models.ForeignKey(Sezon, null=True, on_delete=models.SET_NULL, related_name='loserteam')
    event_date = models.DateField(null=True)
    time = models.FloatField(default=20.0)
    def __str__(self):
        return self.winner.name + " vs " + self.loser.name
    def get_event_date(self):
        return str(self.event_date)

class PentaKill(models.Model):
    player = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='playerpoint')
    game = models.ForeignKey(Game, null=True, on_delete=models.SET_NULL, related_name='gamepoint')
    minute = models.FloatField(default=0.0)
    def __str__(self):
        return "PentaKill: " + self.player.nick + " " + str(self.minute)
