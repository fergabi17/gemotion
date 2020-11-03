from django.db import models


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
    
    
class Game(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    platform = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    genre = models.CharField(max_length=254, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name