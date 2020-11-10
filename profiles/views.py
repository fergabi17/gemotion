from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile

# @login_required
def profile(request):
    """
    Creates a view for the user's profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    reviews = profile.reviews.all()
    
    context = {
        'profile': profile,
        'reviews': reviews
    }
    return render(request, 'profiles/profile.html', context)
