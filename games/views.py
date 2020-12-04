from django.shortcuts import render, get_object_or_404
from .models import Game
from reviews.models import Review

import http.client
import urllib.parse
import json


def index(request):
    """
    Creates a view for the index page (review a game)
    """
    return render(request, 'games/index.html')


def search_game(request):
    """
    Searches for a game title on the RAWG api
    and returns the result of the search on
    the game-list page
    """
    input_game_title = request.POST['game-title']
    result = call_RAWG(request, "search")["results"]
    games_reviewed = list(Review.objects.values_list("game__game_id").distinct())
    games_reviewed = [ i[0] for i in games_reviewed ]
    
    context = {
        "search_term": input_game_title,
        "content": result,
        "games_reviewed": games_reviewed
    }

    return render(request, 'games/game-list.html', context)


def get_or_add_game(request):
    """
    Tries getting the game from gemotion database,
    if it's not there yet it adds it
    returns the game object
    """
    game_id = int(request.POST["game-id"])

    try:
        return Game.objects.get(game_id=game_id)
    except:
        game = call_RAWG(request, "game_details")

        new_game = Game(game_id=game_id, 
                        name=game["name"], 
                        platforms=extract_from_list(game["platforms"], "platform"), 
                        genre=extract_from_list(game["genres"], "name"),
                        description=game["description"], 
                        released=game["released"],
                        background_image=game["background_image"], 
                        background_image_additional=game["background_image_additional"],
                        saturated_color=game["saturated_color"], 
                        dominant_color=game["dominant_color"])

        new_game.save()
        return new_game


def call_RAWG(request, get_type):
    """
    Contacts the RAWG api to search a game
    or to get game details
    """
    if get_type == "search":
        input_game_title = request.POST['game-title']
        game_title = urllib.parse.quote(input_game_title)
        url_end = f"?search={game_title}"
    else:
        game_id = int(request.POST["game-id"])
        url_end = f"/{game_id}"
        
    conn = http.client.HTTPSConnection("rapidapi.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "e930d07731mshe00718d0d6136eap1ae483jsnf6cea31e0367",
        'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }

    conn.request("GET", f"/games{url_end}", headers=headers)
    res = conn.getresponse().read()
    return json.loads(res)


"""
**************************************************** HELPER FUNC
"""

def extract_from_list(sublist, key):
    """
    @list: array
    @key: string
    @returns: string
    Extracts the key values from a list of dicts
    """
    content = ""
    for item in sublist:
        if key == "platform":
            value = item[key]["name"]
        else:
            value = item[key]
        if content == "":
            content = value
        else:
            content = content + ", " + value
    return content