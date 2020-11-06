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
