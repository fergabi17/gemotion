from django.shortcuts import render

# Create your views here.
def review(request):
    """
    Creates a view for the review page
    """
    return render(request, 'reviews/review.html')