
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import requests

from user_profiles.models import Profile
from api.models import Room
from api.models import Player


BASE_URL = 'https://lambda-treasure-hunt.herokuapp.com/api/adv'


@api_view(['GET'])
def init(request):
    user = Profile.objects.filter(user__username=request.user).first()
    headers = {
        'Authorization': f'Token {user.api_token}'
    }
    response = requests.get(f'{BASE_URL}/init', headers=headers)
    response = response.json()

    # player = Player(current_room=response['room_id'])
    # player.save

    return Response(response)


@api_view(['POST'])
def move(request):
    user = Profile.objects.filter(user__username=request.user).first()
    headers = {
        'Authorization': f'Token {user.api_token}'
    }

    data = request.data

    response = requests.post(f'{BASE_URL}/move', headers=headers, json=data)
    response = response.json()
    res_tuple = eval(response['coordinates'])

    room = Room(
        id=response['room_id'],
        title=response['title'],
        description=response['description'],
        terrain=response['terrain'],
        elevation=response['elevation'],
        coordinates=res_tuple,
        x=res_tuple[0],
        y=res_tuple[1]
    )

    player = Player.objects.get(id=1)

    # connect room
    room.connectRooms(data['direction'],
                      player.current_room, response['room_id'])
    # update room
    room.save()

    # update player
    player.current_room = response['room_id']
    player.cooldown = response['cooldown']
    player.save()

    return Response(response)


@api_view(['POST'])
def take(request):
    user = Profile.objects.filter(user__username=request.user).first()
    headers = {
        'Authorization': f'Token {user.api_token}'
    }

    data = json.dumps(request.data)
    response = requests.post(f'{BASE_URL}/take', headers=headers, data=data)

    return Response(response.json())


@api_view(['POST'])
def drop(request):
    user = Profile.objects.filter(user__username=request.user).first()
    headers = {
        'Authorization': f'Token {user.api_token}'
    }
    data = json.dumps(request.data)

    response = requests.post(f'{BASE_URL}/drop', headers=headers, data=data)

    return Response(response.json())


@api_view(['POST'])
def sell(request):
    user = Profile.objects.filter(user__username=request.user).first()
    headers = {
        'Authorization': f'Token {user.api_token}'
    }
    data = json.dumps(request.data)

    response = requests.post(f'{BASE_URL}/sell', headers=headers, data=data)

    return Response(response.json())


@api_view(['POST'])
def confirm_sell(request):
    user = Profile.objects.filter(user__username=request.user).first()
    headers = {
        'Authorization': f'Token {user.api_token}'
    }
    data = json.dumps(requests.data)
    response = requests.post(f'{BASE_URL}/sell', headers=headers, data=data)

    return Response(response.json())


@api_view(['POST'])
def status(request):
    user = Profile.objects.filter(user__username=request.user).first()
    headers = {
        'Authorization': f'Token {user.api_token}'
    }

    response = requests.post(f'{BASE_URL}/status/', headers=headers)

    return Response(response.json())


@api_view(['POST'])
def examine(request):
    user = Profile.objects.filter(user__username=request.user).first()
    headers = {
        'Authorization': f'Token {user.api_token}'
    }
    data = json.dumps(request.data)
    response = requests.post(f'{BASE_URL}/examine', headers=headers, data=data)

    return Response(response.json())


@api_view(['POST'])
def change_name(request):
    user = Profile.objects.filter(user__username=request.user).first()
    headers = {
        'Authorization': f'Token {user.api_token}'
    }
    data = json.dumps(request.data)
    response = requests.post(
        f'{BASE_URL}/change_name', headers=headers, data=data)

    return Response(response.json())


@api_view(['POST'])
def pray(request):
    user = Profile.objects.filter(user__username=request.user).first()
    headers = {
        'Authorization': f'Token {user.api_token}'
    }
    response = requests.post(f'{BASE_URL}/pray', headers=headers)

    return Response(response.json())


@api_view(['POST'])
def flight(request):
    user = Profile.objects.filter(user__username=request.user).first()
    headers = {
        'Authorization': f'Token {user.api_token}'
    }
    data = json.dumps(request.data)

    response = requests.post(f'{BASE_URL}/fly', headers=headers, data=data)

    return Response(response.json())


@api_view(['POST'])
def dash(request):
    user = Profile.objects.filter(user__username=request.user).first()
    headers = {
        'Authorization': f'Token {user.api_token}'
    }
    data = json.dumps(request.data)
    response = requests.post(f'{BASE_URL}/dash', headers=headers, data=data)

    return Response(response.json())


@api_view(['POST'])
def check_exits(request):
    user = Profile.objects.filter(user__username=request.user).first()

    data = request.data
    room = Room.objects.get(id=data['current_room'])
    exits = {
        'n': room.n_to,
        'e': room.e_to,
        's': room.s_to,
        'w': room.w_to,
    }
    return Response(exits)
