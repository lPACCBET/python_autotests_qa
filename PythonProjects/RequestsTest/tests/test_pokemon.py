import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '90c75ee11d5fd2dfd89d173bdad6dcf6'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '11378'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_respounce():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'lPACCBET'
