
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
from collections import Counter, OrderedDict
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
        categories_model = serializers.serialize("json", categories_model)
        categories_model = json.loads(categories_model)

        context = {
            'game': game,
            'emotions': json.dumps(emotions_pk),
            'categories': categories_array,
            'categories_model': categories_model,
            'form': form,

            'emotions_model': emotions_model
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
        user_game_reviews = Review.objects.filter(game=game,
                                                  user_profile=profile)
        reviews_emotions = list(
            user_game_reviews.values_list('emotion__name', flat=True))

        for pk in result:
            emotion = get_object_or_404(Emotion, pk=pk)
            if str(emotion) not in reviews_emotions:
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
                                user_profile=profile,
                                played=user_played,
                                emotion=emotion)
            new_review.save()
    return redirect(reverse('profile'))


def review_list(request):
    """
    Renders the list of games last reviewed on the webapp
    """
    reviews = Review.objects.values_list("game", "date").order_by('-date')
    # reviews = Review.objects.values_list("game").filter(emotion__category__name='happy').order_by('-date')
    presented_games = []
    for review in reviews:
        if not any(review[0] in i for i in presented_games):
            presented_games.append(review)
            if len(presented_games) >= 10:
                break

    games = []
    for game in presented_games:
        game_dict = get_object_or_404(Game, pk=game[0])
        last_reviewed = game[1]
        games.append((game_dict, last_reviewed))
    context = {
        'games': games,
    }
    return render(request, 'reviews/review_list.html', context)


def game_reviews(request, game_id):
    """
    Renders the game details page
    with the statistics from reviews
    """
    path = request.META.get('HTTP_REFERER')

    if "/game_list/" in path:
        game = get_object_or_404(Game, game_id=game_id)
        game_id = game.pk
    else:
        game = get_object_or_404(Game, pk=game_id)
        
    reviews = Review.objects.filter(game=game_id)
    users = reviews.values_list("user_profile__user__username").distinct()
    
    emotions = reviews.values_list("emotion__name")
    emotions_count = Counter(emotions).most_common(10)
    emotions_count = { item[0][0] : item[1] for item in emotions_count }
    emotions_percentage = get_dict_percentages(emotions_count, len(reviews))
    
    categories_model = Category.objects.all()
    categories_final = {}
    for category in categories_model:
        categories_final[str(category)] = 0

    categories = reviews.values_list("emotion__category__name")
    categories_count = Counter(categories).most_common()
    categories_count = { item[0][0] : item[1] for item in categories_count }

    for item in categories_final:
        if item in categories_count:
            categories_final[item] = categories_count[item]
    categories_percentage = get_dict_percentages(categories_final, len(reviews))
    
    played = reviews.values_list("played", "user_profile__user__username").distinct()
    played_count = Counter(True in i for i in played)
    played_count = { 'played': played_count[True], 'watched': played_count[False] }
    played_percentage = get_dict_percentages(played_count, sum(played_count.values()))
    
    context= {
        'game': game,
        'users_reviewed': len(users),
        'categories_percentage': json.dumps(categories_percentage),
        'emotions_percentage': json.dumps(emotions_percentage),
        'played_percentage': played_percentage,
    }
    return render(request, 'reviews/game_reviews.html', context)


# ------------------------------------------------------- Helper functions

def percentage(part, whole):
  return int(100 * part/whole)

def get_dict_percentages(numbers_dict, reviews):
    for key in numbers_dict:
        numbers_dict[key] = percentage(numbers_dict[key], reviews)
    return numbers_dict