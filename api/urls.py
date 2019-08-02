from django.urls import path

from .views import init, move, take, drop, sell, confirm_sell, status, examine, change_name, pray, flight, dash, check_exits

urlpatterns = [
    path('init', init, name='game-init'),
    path('move', move, name='game-move'),
    path('take', take, name="game-take"),
    path('drop', drop, name="game-drop"),
    path('sell', sell, name="game-sell"),
    path('sell/confirm', confirm_sell, name="game-sell-confirm"),
    path('status', status, name="game-status"),
    path('examine', examine, name="game-examine"),
    path('change_name', change_name, name="game-change_name"),
    path('pray', pray, name="game-pray"),
    path('fly', flight, name="game-fly"),
    path('dash', dash, name="game-dash"),
    path('check_exits', check_exits, name="check-exits")
]
