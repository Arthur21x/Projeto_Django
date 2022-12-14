import requests

for pokemon in range(1, 901):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()

    if len(response['types']) == 2:
        type1 = response['types'][0]['type']['name']
        type2 = response['types'][1]['type']['name']

        print(f"INSERT INTO pokemon_pokemontype"
              f" VALUES ('{pokemon}', '{type1}', '{type2}');")
    else:
        type1 = response['types'][0]['type']['name']
        print(f"INSERT INTO pokemon_pokemontype"
              f" VALUES ('{pokemon}', '{type1}', 'NULO');")
