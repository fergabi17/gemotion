from django.db import models
    
    
class Game(models.Model):
    game_id = models.IntegerField()
    name = models.CharField(max_length=254)
    platforms = models.CharField(max_length=254)
    genre = models.CharField(max_length=254, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    released = models.CharField(max_length=254, null=True, blank=True)
    background_image = models.URLField(max_length=1024, null=True, blank=True)
    background_image_additional = models.URLField(max_length=1024, null=True, blank=True)
    saturated_color = models.CharField(max_length=254, null=True, blank=True)
    dominant_color = models.CharField(max_length=254, null=True, blank=True)
    

    def __str__(self):
        return self.name