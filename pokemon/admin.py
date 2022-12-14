from django.contrib import admin
from .models import PokemonSprite, PokemonType, PokemonAbilitis, PokemonEvolution, PokemonInfo


# Register your models here.

class AbilitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'Ability1', 'Ability2', 'Ability3')


class SpriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'front_default', 'back_default', 'shiny',
                    'front_shiny', 'dream_world', 'official_artwork')


admin.site.register(PokemonSprite, SpriteAdmin)
admin.site.register(PokemonType)
admin.site.register(PokemonAbilitis, AbilitiesAdmin)
admin.site.register(PokemonEvolution)
admin.site.register(PokemonInfo)
