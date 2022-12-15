from django.shortcuts import render
from .models import PokemonInfo
from django.core.paginator import Paginator
import requests


# Create your views here.
def index(request):
    Pokemons = PokemonInfo.objects.all()
    paginator = Paginator(Pokemons, 80)

    page = request.GET.get('page')
    Pokemons = paginator.get_page(page)
    return render(request, 'pokemon/index.html', {'Pokemon': Pokemons})


def busca(request):
    pokemon = request.GET.get('pokemon')
    Pokemons = PokemonInfo.objects.order_by('-id').filter(name=pokemon.lower())
    paginator = Paginator(Pokemons, 80)

    page = request.GET.get('page')
    Pokemons = paginator.get_page(page)
    return render(request, 'pokemon/busca.html', {'Pokemon': Pokemons})

