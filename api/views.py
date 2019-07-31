
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from user_profiles.models import Profile
from api.models import Room


BASE_URL = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/'


@api_view(['GET'])
def init(request):
    user = Profile.objects.filter(user__username=request.user)[0]
    headers = {
        'Authorization': f'Token {user.api_token}'
    }
    response = requests.get(f'{BASE_URL}/init', headers=headers)

    return Response(response.json())


@api_view(['POST'])
def move(request):
    user = Profile.objects.filter(user__username=request.user)[0]
    headers = {
        'Authorization': f'Token {user.api_token}'
    }
    data = request.data
    response = requests.post(f'{BASE_URL}/move', headers=headers, json=data)

    return Response(response.json())

