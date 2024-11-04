import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '90c75ee11d5fd2dfd89d173bdad6dcf6'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}


body_create = {
    "name": "lPACCBET",
    "photo_id": 1
}

body_changeName = {
    "pokemon_id": "109262",
    "name": "lPACCBET2",
    "photo_id": 1
} 

body_pok_in_pokeball = {
    "pokemon_id": "109262"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response.text)


response_changeName = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_changeName)
print(response_changeName.text)

response_pok_in_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pok_in_pokeball)
print(response_pok_in_pokeball.text)


