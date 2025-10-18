import requests

base_url="https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{name}" # get the api url here
    response=requests.get(url) # storing the reponse

    if response.status_code == 200:
        pokemon_data= response.json()
        return pokemon_data
    else:
        print(f"Failed to retieve the data : Error Code {response.status_code}")
    

pokename_name="pikachu"
pokemon_info=get_pokemon_info(pokename_name)

if pokemon_info:
    print(f"{pokemon_info['name']}") # double quote  with single quote inside


