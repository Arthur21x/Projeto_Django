import requests

for pokemon in range(1, 901):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()
    name = response['name']
    order = response['order']
    weight = response['weight']
    height = response['height']

    print(f"INSERT INTO pokemon_pokemoninfo"
          f" VALUES ('{pokemon}', '{name}', '{order}', '{weight}', '{height}', '{pokemon}', '{pokemon}', '{pokemon}', '{pokemon}');")
