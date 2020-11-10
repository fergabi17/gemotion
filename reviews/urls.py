from django.urls import path
from . import views

urlpatterns = [
    path('', views.review, name='review'),
    path('post_review/', views.post_review, name='post_review')
]