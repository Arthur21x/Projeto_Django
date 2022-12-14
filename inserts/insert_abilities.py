import requests

for pokemon in range(1, 901):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()
    habilidade = response['abilities']
    if len(habilidade) >= 3:
        Ability1 = habilidade[0]['ability']['name']
        Ability2 = habilidade[1]['ability']['name']
        Ability3 = habilidade[2]['ability']['name']
        print(f"INSERT INTO pokemon_pokemonabilitis"
              f" (id, Ability1, Ability2, Ability3)"
              f" VALUES ('{pokemon}', '{Ability1}', '{Ability2}', '{Ability3}');")
        continue
    elif len(habilidade) == 2:
        Ability1 = habilidade[0]['ability']['name']
        Ability2 = habilidade[1]['ability']['name']
        print(f"INSERT INTO pokemon_pokemonabilitis"
              f" (id, Ability1, Ability2)"
              f" VALUES ('{pokemon}', '{Ability1}', '{Ability2}');")
    else:
        Ability1 = habilidade[0]['ability']['name']
        print(f"INSERT INTO pokemon_pokemonabilitis"
              f" (id, Ability1)"
              f" VALUES ('{pokemon}', '{Ability1}');")
