from django.shortcuts import render
from .models import PokemonInfo
from django.core.paginator import Paginator
import requests


# Create your views here.
def index(request):
    Pokemons = PokemonInfo.objects.all()
    paginator = Paginator(Pokemons, 25)

    page = request.GET.get('page')
    Pokemons = paginator.get_page(page)
    return render(request, 'pokemon/index.html', {'Pokemon': Pokemons})


def pokemon(request, identificador):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{identificador}').json()
    return render(request, 'pokemon/pokemon.html', {'response', response})

