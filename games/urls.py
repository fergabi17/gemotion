from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='games'),
    path('game_list/', views.search_game, name='game_list')
]