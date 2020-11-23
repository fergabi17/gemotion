from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('delete_review/<game>/', views.delete_review, name='delete_review'),
    path('payment/', views.payment, name='payment'),
]