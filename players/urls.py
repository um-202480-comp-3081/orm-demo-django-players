from django.urls import path
from . import views

app_name = 'players'

urlpatterns = [
    path('', views.player_list, name='player_list'),
    path('<int:id>', views.player_detail, name='player_detail'),
]
