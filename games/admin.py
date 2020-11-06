from django.contrib import admin
from .models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = (
        'game_id',
        'name',
        'platforms',
        'genre',
        'description',
        'released',
        'background_image',
        'background_image_additional',
        'saturated_color',
        'dominant_color'
    )
    
    ordering = ('name',)
    
admin.site.register(Game, GameAdmin)

