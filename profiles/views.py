from django.shortcuts import render

def profiles(request):
    """
    Creates a view for the index
    """
    return render(request, 'profiles/profile.html')
