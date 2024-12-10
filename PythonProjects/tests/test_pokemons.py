import pytest
import requests

URL = 'https://api.pokemonbattle.ru/v2'
token = '03d4eea5260cc0c6dfb5b77a2fe9c061'
header = {'Content-Type' : 'application/json', 'trainer_token': token}
trainer_id = '11514'

def test_status_cod():
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id': trainer_id})
    assert response.status_code == 200

def test_response():
    response_get = requests.get(url = f'{URL}/trainers', params={'trainer_id': trainer_id})
    assert response_get.json()["data"][0]["trainer_name"] == 'Gemini'


