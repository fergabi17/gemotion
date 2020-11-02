from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Creates a view for the index
    """
    return render(request, 'games/index.html')