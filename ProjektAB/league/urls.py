from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


app_name = 'league'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:league_id>/', views.league_sezons, name='league_sezons'),
    path('<int:sezon_id>/sezon_teams', views.sezon_teams, name='sezon_teams'),
    path('<int:team_id>/team', views.team, name='team'),
    path('<int:player_id>/player', views.player, name='player'),
    path('<int:coach_id>/coach', views.coach, name='coach'),
    url('signup/', views.signup, name='signup'),
    path('player_upload', views.player_upload_view, name='player_upload'),
    path('<int:player_id>/player_update', views.player_update_view, name='player_update'),
    path('<int:player_id>/player_delete', views.player_delete_view, name='player_delete'),
    path('coach_upload', views.coach_upload_view, name='coach_upload'),
    path('<int:coach_id>/coach_update', views.coach_update_view, name='coach_update'),
    path('<int:coach_id>/coach_delete', views.coach_delete_view, name='coach_delete'),
    path('team_upload', views.team_upload_view, name='team_upload'),
    path('<int:team_id>/team_update', views.team_update_view, name='team_update'),
    path('<int:team_id>/team_delete', views.team_delete_view, name='team_delete'),
    path('game_upload', views.game_upload_view, name='game_upload'),
    path('<int:game_id>/game_update', views.game_update_view, name='game_update'),
    path('<int:game_id>/game_delete', views.game_delete_view, name='game_delete'),
    path('teamhistory_upload', views.teamHistory_upload_view, name='teamhistory_upload'),
    path('pentakill_upload', views.pentakill_upload_view, name='pentakill_upload'),
    path('sezon_upload', views.sezon_upload_view, name='sezon_upload'),
    path('<int:sezon_id>/sezon_update', views.sezon_update_view, name='sezon_update'),
    path('<int:sezon_id>/sezon_delete', views.sezon_delete_view, name='sezon_delete'),
    path('league_upload', views.league_upload_view, name='league_upload'),
    path('<int:league_id>/league_update', views.league_update_view, name='league_update'),
    path('<int:league_id>/league_delete', views.league_delete_view, name='league_delete'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)