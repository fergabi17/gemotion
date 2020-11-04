from django.shortcuts import render


# FOR GAME SEARCH
import http.client
import urllib.parse
import json


def index(request):
    """
    Creates a view for the index
    """
    return render(request, 'games/index.html')


def search_game(request):
    """
    """


    input_game_title = request.POST['game-title']
    game_title = urllib.parse.quote(input_game_title)

    conn = http.client.HTTPSConnection("rapidapi.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "e930d07731mshe00718d0d6136eap1ae483jsnf6cea31e0367",
        'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
        }

    conn.request("GET", f"/games?search={game_title}", headers=headers)

    res = conn.getresponse()
    data = res.read()
    result = json.loads(data)["results"]

    
    context = {
        "search_term": input_game_title,
        "content": result
    }
    
    return render(request, 'games/game-list.html', context)