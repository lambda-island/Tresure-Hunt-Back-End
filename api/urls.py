from django.urls import path

from .views import init, move

urlpatterns = [
    path('init', init, name='game-init'),
    path('move', move, name='game-move'),
]