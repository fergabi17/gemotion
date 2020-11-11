from django.db import models
from games.models import Game
from profiles.models import UserProfile

class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=254)
    
    def __str__(self):
        return self.name


class Emotion(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')
    emotion = models.ForeignKey(Emotion, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.game}'