import requests
import json

URL = 'https://animalsrestapi.azurewebsites.net/api/animals/'

def post(animal):
    animalToAdd = json.loads(animal)


    response = requests.post(URL, json = animalToAdd)
    data = response.json()
    return data, response