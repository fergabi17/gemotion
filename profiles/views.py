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

    top_emotions = reviews.values_list('emotion__name').annotate(
        emotion_count=Count('emotion')).order_by('-emotion_count')
    games_top_emotions = reviews.filter(emotion__name=top_emotions[0][0])
    games_top_emotions = games_top_emotions.values_list('game__name', flat=True).distinct()
    
    top_categories = reviews.values_list('emotion__category__name').annotate(
        category_count=Count('emotion__category__name')).order_by('-category_count')
    games_top_categories = reviews.filter(emotion__category__name=top_categories[0][0])
    games_top_categories = games_top_categories.values_list('game__name', flat=True).distinct()
    
    last_review = reviews.order_by('-date').first()
    
    context = {
        'profile': profile,
        
        'reviews': len(games),
        'game_names': games,
        'top_emotion': top_emotions[0][0],
        'games_top_emotions': games_top_emotions,
        'top_category': top_categories[0][0],
        'games_top_category': games_top_categories,
        'last_review': last_review
    }

    return render(request, 'profiles/profile.html', context)
