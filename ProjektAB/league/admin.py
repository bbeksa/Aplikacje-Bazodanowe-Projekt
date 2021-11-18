from django.contrib import admin

from .models import PentaKill, Player, Game, League, LeagueClassification, Coach, TeamHistory, Team, Sezon




admin.site.register(League)
admin.site.register(Sezon)
admin.site.register(Player)
admin.site.register(PentaKill)
admin.site.register(Game)
admin.site.register(LeagueClassification)
admin.site.register(Coach)
admin.site.register(TeamHistory)
admin.site.register(Team)
