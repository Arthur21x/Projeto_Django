from django.contrib import admin
from .models import PokemonSprite, PokemonType, PokemonAbilitis, PokemonEvolution, PokemonInfo


# Register your models here.

class AbilitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'Ability1', 'Ability2', 'Ability3')
    list_filter = ('id', 'Ability1', 'Ability2', 'Ability3')


class SpriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'front_default', 'back_default', 'shiny',
                    'front_shiny', 'dream_world', 'official_artwork')


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'Type1', 'Type2')
    list_filter = ('id', 'Type1', 'Type2')


admin.site.register(PokemonSprite, SpriteAdmin)
admin.site.register(PokemonType, TypeAdmin)
admin.site.register(PokemonAbilitis, AbilitiesAdmin)
admin.site.register(PokemonEvolution)
admin.site.register(PokemonInfo)
