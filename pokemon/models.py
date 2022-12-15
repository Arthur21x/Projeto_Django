from django.db import models


# Create your models here.
class PokemonSprite(models.Model):
    back_default = models.CharField(max_length=255)
    shiny = models.CharField(max_length=255)
    front_shiny = models.CharField(max_length=255)
    front_default = models.CharField(max_length=255)
    dream_world = models.CharField(max_length=255)
    official_artwork = models.CharField(max_length=255)


class PokemonType(models.Model):
    Type1 = models.CharField(max_length=255)
    Type2 = models.CharField(max_length=255, blank=True)


class PokemonAbilitis(models.Model):
    Ability1 = models.CharField(max_length=255)
    Ability2 = models.CharField(max_length=255, blank=True)
    Ability3 = models.CharField(max_length=255, blank=True)


class PokemonEvolution(models.Model):
    Evolution1 = models.CharField(max_length=255)
    Evolution2 = models.CharField(max_length=255, blank=True)
    Evolution3 = models.CharField(max_length=255, blank=True)
    Evolution4 = models.CharField(max_length=255, blank=True)
    Evolution5 = models.CharField(max_length=255, blank=True)
    Evolution6 = models.CharField(max_length=255, blank=True)
    Evolution7 = models.CharField(max_length=255, blank=True)
    Evolution8 = models.CharField(max_length=255, blank=True)
    Evolution9 = models.CharField(max_length=255, blank=True)


class PokemonInfo(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    Evolution = models.ForeignKey(PokemonEvolution, on_delete=models.CASCADE, related_name='evolution')
    Ability= models.ForeignKey(PokemonAbilitis, on_delete=models.CASCADE, related_name='ability')
    Type = models.ForeignKey(PokemonType, on_delete=models.CASCADE, related_name='type')
    Sprite = models.ForeignKey(PokemonSprite, on_delete=models.CASCADE, related_name='sprite')
