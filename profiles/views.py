from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from games.models import Game
from reviews.models import Category, Emotion
from django.db.models import Count, F

# @login_required


def profile(request):
    """
    Creates a view for the user's profile
    presenting data about reviews
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    reviews = profile.reviews.all()

    games = reviews.values_list('game__name', flat=True).distinct()
    game_names = games

    top_emotions = reviews.values_list('emotion__name').annotate(
        emotion_count=Count('emotion')).order_by('-emotion_count')
    top_categories = reviews.values_list('emotion__category__name').annotate(
        category_count=Count('emotion__category__name')).order_by('-category_count')

    context = {
        'profile': profile,
        
        'reviews': len(games),
        'game_names': game_names,
        'top_emotion': top_emotions[0][0],
        'top_category': top_categories[0][0]
    }

    return render(request, 'profiles/profile.html', context)
