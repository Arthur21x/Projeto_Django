import requests

for pokemon in range(1, 901):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()

    back_default = response['sprites']['back_default']
    shiny = response['sprites']['back_shiny']
    front_shiny = response['sprites']['front_shiny']
    front_default = response['sprites']['front_default']
    dream_world = response['sprites']['other']['dream_world']['front_default']
    official_artwork = response['sprites']['other']['official-artwork']['front_default']
    print(f"INSERT INTO pokemon_pokemonsprite"
          f" VALUES ('{pokemon}', '{back_default}', '{shiny}', '{front_shiny}', '{front_default}', '{dream_world}', '{official_artwork}');")
