
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
from .models import Emotion, Category, Review
from profiles.models import UserProfile
from games.models import Game
from games.views import get_or_add_game
from .forms import ReviewForm
import json


def review(request):
    """
    Gets the game object and
    Creates a view for the review page
    """

    if "term" in request.GET:
        em = Emotion.objects.filter(name__icontains=request.GET.get('term'))
        cat = Category.objects.filter(
            name__istartswith=request.GET.get('term'))
        emotions = list()
        for emotion in em:
            emotions.append(emotion.name)
        for emotion in cat:
            emotions.append(emotion.name)
        return JsonResponse(emotions, safe=False)
    else:
        game = get_or_add_game(request)
        form = ReviewForm(request.POST)

        emotions_model = Emotion.objects.all()
        emotions_model = serializers.serialize("json", emotions_model)
        emotions_model = json.loads(emotions_model)

        emotions_pk = {}
        for emotion in emotions_model:
            emotions_pk[emotion['fields']['name']] = emotion['pk']

        categories_model = Category.objects.all()
        categories_array = []
        for category in categories_model:
            categories_array.append(str(category))
        categories = json.dumps(categories_array)

        context = {
            'game': game,
            'emotions': json.dumps(emotions_pk),
            'categories': categories,
            'form': form
        }

        return render(request, 'reviews/review.html', context)


def post_review(request):
    """
    Posts all the emotions as single inputs in the database
    """
    result = request.POST['pk_list']

    result = json.loads(result)
    game_id = request.POST['game-id']
    user_played = request.POST.get('played')

    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        game = get_object_or_404(Game, pk=game_id)
        for pk in result:
            emotion = get_object_or_404(Emotion, pk=pk)
            new_review = Review(game=game,
                                user_profile=profile,
                                played=user_played,
                                emotion=emotion)
            new_review.save()
    else:
        game = get_object_or_404(Game, pk=game_id)
        for pk in result:
            emotion = get_object_or_404(Emotion, pk=pk)
            new_review = Review(game=game,
                                played=user_played,
                                emotion=emotion)
            new_review.save()
    return redirect(reverse('profile'))

