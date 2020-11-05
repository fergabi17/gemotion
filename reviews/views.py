
from django.shortcuts import render, get_object_or_404
from games.models import Game
from games.views import get_or_add_game


def review(request):
    """
    Creates a view for the review page
    """
    game = get_or_add_game(request)

    # game_id = int(request.POST["game-id"])
    context = {
        'game': game
    }

    return render(request, 'reviews/review.html', context)


