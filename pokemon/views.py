from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    response = requests.get('https://pokeapi.co/api/v2/pokemon').json()
    return render(request, 'pokemon/index.html', {'response': response})


def pokemon(request, identificador):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{identificador}').json()
    return render(request, 'pokemon/pokemon.html', {'response', response})

