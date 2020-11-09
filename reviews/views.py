
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Emotion, Category
from games.views import get_or_add_game
import json


def review(request):
    """
    Gets the game object and
    Creates a view for the review page
    """
    
        
    if "term" in request.GET:
        em = Emotion.objects.filter(name__icontains=request.GET.get('term'))
        cat = Category.objects.filter(name__istartswith=request.GET.get('term'))
        emotions = list()
        for emotion in em:
            emotions.append(emotion.name)
        for emotion in cat:
            emotions.append(emotion.name)
        return JsonResponse(emotions, safe=False)
    else:
        game = get_or_add_game(request)
        emotions_model = Emotion.objects.all()
        categories_model = Category.objects.all()
        emotions_array = []
        categories_array = []
        for emotion in emotions_model:
            emotions_array.append(str(emotion))
        for category in categories_model:
            categories_array.append(str(category))
        emotions = json.dumps(emotions_array)
        categories = json.dumps(categories_array)
        context = {
            'game': game,
            'emotions': emotions,
            'categories': categories
        }

        return render(request, 'reviews/review.html', context)



    


