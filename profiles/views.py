from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from collections import Counter
from .models import UserProfile
from games.models import Game
from reviews.models import Category, Emotion, Review
from django.db.models import Count, F
from os import path
import os
import stripe

if path.exists("profiles/env.py"):
    from profiles import env


def profile(request):
    """
    Creates a view for the user's profile
    presenting data about reviews
    """
    
    categories_model = Category.objects.all()
    categories_final = {}
    for category in categories_model:
        categories_final[str(category)] = 0
        
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        reviews = profile.reviews.all()
        last_review = reviews.order_by('-date').first()


        games = reviews.values('game__name', 'game').distinct()
        games_names = reviews.values_list('game__name', flat=True).distinct()
        games_reviewed = len(games_names)


        top_emotions = reviews.values_list('emotion__name').annotate(
            emotion_count=Count('emotion')).order_by('-emotion_count')
        top_emotion = top_emotions[0][0] if len(top_emotions) > 0 else "None"
        games_top_emotions = reviews.filter(emotion__name=top_emotion)
        games_top_emotions = games_top_emotions.values_list('game__name', flat=True).distinct()[:5]
        
        
        top_categories = reviews.values_list('emotion__category__name').annotate(
            category_count=Count('emotion__category__name')).order_by('-category_count')
        top_category = top_categories[0][0] if len(top_categories) > 0 else "None"
        games_top_categories = reviews.filter(emotion__category__name=top_category)
        games_top_categories = games_top_categories.values_list('game__name', flat=True).distinct()[:5]
        
        categories = reviews.values_list("emotion__category__name")
        categories_count = Counter(categories).most_common()
        categories_count = {item[0][0]: item[1] for item in categories_count}

        for item in categories_final:
            if item in categories_count:
                categories_final[item] = categories_count[item]
        categories_percentage = get_dict_percentages(
            categories_final, len(reviews))
              
    else:
        profile = "user"
        games_reviewed = "?"
        games = "?"
        top_emotion = "unknown"
        games_names = "?"
        games_top_emotions = "?"
        top_category = "secret"
        games_top_categories = "?"
        last_review = "maybe Candy Crush"
        categories_percentage = categories_final
        
    context = {
        'profile': profile,
        'games': games,
        'reviews': games_reviewed,
        'game_names': games_names,
        'top_emotion': top_emotion,
        'games_top_emotions': games_top_emotions,
        'top_category': top_category,
        'games_top_category': games_top_categories,
        'last_review': last_review,
        'categories_percentage': categories_percentage
    }

    return render(request, 'profiles/profile.html', context)


def delete_review(request, game):
    """
    Deletes a review from the database
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    game = get_object_or_404(Game, pk=game)
    reviews = Review.objects.filter(game=game,
                                    user_profile=profile)
    reviews.delete()
    messages.warning(request, f'{game} was deleted from your reviews')
    return redirect(reverse('profile'))


def payment(request):
    """
    Renders the payment page
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    stripe_total = 500
    
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
    
    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }
    return render(request, 'profiles/payment.html', context)


def donated(request):
    """
    Changes the user status to donated
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    profile.donated = True
    profile.save()
    return redirect(reverse('profile'))

# ------------------------------------------------------- Helper functions

def percentage(part, whole):
    return int(100 * part/whole)


def get_dict_percentages(numbers_dict, reviews):
    for key in numbers_dict:
        numbers_dict[key] = percentage(numbers_dict[key], reviews)
    return numbers_dict