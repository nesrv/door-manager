from time import time
from django.shortcuts import render, get_object_or_404
import aiohttp

from django.http import JsonResponse

from authlib.jose import JsonWebToken

from .setting2 import CONTROLLERS, JWT_PRIVATE_KEY, JWT_ALGORITHM

# from .settings2 import CONTROLLERS, JWT_PRIVATE_KEY, JWT_ALGORITHM

ACCESS_TOKEN_TIME_TOLERANCE = 3600
jwt = JsonWebToken([JWT_ALGORITHM])

from .models import *

menu = [
    {'title': "Door control", 'url_name': 'index'},
    {'title': "User", 'url_name': 'user'},
    {'title': "History", 'url_name': 'history'},
    {'title': "Administrator", 'url_name': 'admin'}
]


def index(request):
    context = {
        'title': "Access Manager",
        'subtitle': 'Door opening and control',
        'CONTROLLERS': CONTROLLERS
    }
    return render(request, 'interface/index.html', context)


def user(request):
    users = User.objects.all()
    door = Door.objects.all()
    context = {'title': "Access Manager",
               'subtitle': 'User administration',
               'users': users,
               'doors': door
               }
    return render(request, 'interface/user.html', context)


def history(request):
    context = {'title': "Access Manager",
               'subtitle': 'History of logs'
               }
    return render(request, 'interface/history.html', context)


async def controller_determinant(request, path, door_name):
    url = [(controller['url']) for controller in CONTROLLERS if controller['name'] == door_name][0] + "/" + path
    current_timestamp = int(time())

    claims = {
        'iss': 'org.netica',
        'type': 'grant-access',
        'iat': current_timestamp,
        'nbf': current_timestamp - ACCESS_TOKEN_TIME_TOLERANCE,
        'exp': current_timestamp + ACCESS_TOKEN_TIME_TOLERANCE,
    }
    jwt_token = jwt.encode({'alg': JWT_ALGORITHM}, claims, JWT_PRIVATE_KEY).decode('ascii')

    async with aiohttp.ClientSession() as session:
        response = await session.post(
            url=url,
            headers={
                'Authorization': f'Bearer {jwt_token}',
            },
        )
        resp = await response.json()
        print(resp)
        return JsonResponse(resp)

        # return web.json_response({
        #     'ok': False,
        #     'error': "Access denied, IndexError",
        # }, status=404)
        # print(await response.json())
        # return web.json_response(response)

    # context = {'title': path, 'CONTROLLERS': CONTROLLERS, }
    #
    # return render(request, 'index.html', context)
    # # return HttpResponse("You're looking at question %s." % question_id)
