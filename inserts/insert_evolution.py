import requests


def evolucao(response, index):
    try:
        evolution = requests.get(response['chain']['evolves_to'][index]['species']['url']).json()
    except IndexError:
        evolution = 'NULO'
    return evolution


for pokemon in range(1, 901):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()
    species = requests.get(response['species']['url']).json()
    evolution = requests.get(species['evolution_chain']['url']).json()
    evoution1 = requests.get(evolution['chain']['species']['url']).json()
    evolution1 = requests.get(evoution1['varieties'][0]['pokemon']['url']).json()
    evolution1 = evolution1['sprites']['front_default']
    try:
        evolution2 = evolucao(evolution, 0)
        evolution2 = requests.get(evolution2['varieties'][0]['pokemon']['url']).json()
        evolution2 = evolution2['sprites']['front_default']
    except (IndexError, TypeError):
        evolution2 = 'NULO'
    try:
        evolution3 = requests.get(evolution['chain']['evolves_to'][0]['evolves_to'][0]['species']['url']).json()
        evolution3 = requests.get(evolution3['varieties'][0]['pokemon']['url']).json()
        evolution3 = evolution3['sprites']['front_default']
    except (TypeError,IndexError):
        try:
            evolution3 = evolucao(evolution, 1)
            evolution3 = requests.get(evolution3['varieties'][0]['pokemon']['url']).json()
            evolution3 = evolution3['sprites']['front_default']
        except (IndexError, TypeError):
            evolution3 = 'NULO'
    try:
        evolution4 = evolucao(evolution, 2)
        evolution4 = requests.get(evolution4['varieties'][0]['pokemon']['url']).json()
        evolution4 = evolution4['sprites']['front_default']
    except (IndexError, TypeError):
        evolution4 = 'NULO'
    try:
        evolution5 = evolucao(evolution, 3)
        evolution5 = requests.get(evolution5['varieties'][0]['pokemon']['url']).json()
        evolution5 = evolution5['sprites']['front_default']
    except (IndexError, TypeError):
        evolution5 = 'NULO'
    try:
        evolution6 = evolucao(evolution, 4)
        evolution6 = requests.get(evolution6['varieties'][0]['pokemon']['url']).json()
        evolution6 = evolution6['sprites']['front_default']
    except (IndexError, TypeError):
        evolution6 = 'NULO'
    try:
        evolution7 = evolucao(evolution, 5)
        evolution7 = requests.get(evolution7['varieties'][0]['pokemon']['url']).json()
        evolution7 = evolution7['sprites']['front_default']
    except (IndexError,TypeError):
        evolution5 = 'NULO'
    try:
        evolution8 = evolucao(evolution, 6)
        evolution8 = requests.get(evolution8['varieties'][0]['pokemon']['url']).json()
        evolution8 = evolution8['sprites']['front_default']
    except (IndexError, TypeError):
        evolution8 = 'NULO'

    try:
        evolution9 = evolucao(evolution, 7)
        evolution9 = requests.get(evolution9['varieties'][0]['pokemon']['url']).json()
        evolution9 = evolution9['sprites']['front_default']
    except (IndexError, TypeError):
        evolution9 = 'NULO'

    print(f"INSERT INTO pokemon_pokemonevolution"
          f" VALUES ('{pokemon}', '{evolution1}', '{evolution2}', '{evolution3}', '{evolution4}', '{evolution5}', '{evolution6}', '{evolution7}', '{evolution8}', '{evolution9}');")
