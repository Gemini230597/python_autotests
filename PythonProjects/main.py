import requests

URL = 'https://api.pokemonbattle.ru/v2'
token = '03d4eea5260cc0c6dfb5b77a2fe9c061'
header = {'Content-Type' : 'application/json', 'trainer_token': token}

body_create = {
    "name": "Чапалах3",
    "photo_id": 23
}

response_create = requests.post(url= f'{URL}/pokemons', headers = header, json = body_create)
print (response_create.text)


body_change = {
    "pokemon_id": "156141",
    "name": "Чарманжер",
    "photo_id": 23
}

response_change = requests.put(url= f'{URL}/pokemons', headers = header, json = body_change)
print (response_change.text)


body_add = {
    "pokemon_id": "156141"
}

response_add = requests.post(url= f'{URL}/trainers/add_pokeball', headers = header, json = body_add)
print (response_add.text)