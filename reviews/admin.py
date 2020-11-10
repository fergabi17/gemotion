from django.contrib import admin
from .models import Category, Emotion, Review

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )
    ordering = ('pk',)

class CategoryEmotion(admin.ModelAdmin):
    list_display = (
        'name',
        'category'
    )
    
class CategoryReview(admin.ModelAdmin):
    list_display = (
        'date',
        'game',
        'user_profile',
        'emotion'
    ) 

admin.site.register(Review, CategoryReview)    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Emotion, CategoryEmotion)