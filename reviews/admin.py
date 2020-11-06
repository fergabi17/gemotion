from django.contrib import admin
from .models import Category, Emotion

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

    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Emotion, CategoryEmotion)