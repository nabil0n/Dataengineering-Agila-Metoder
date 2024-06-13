from pathlib import Path
import os
import random
import json

def clear_pokebelt():
    """
    This function clears the pokebelt
    """
    path = Path("pokedata/pokebelt")
    path.mkdir(exist_ok=True, parents=True)
    for filename in os.listdir(path):
        os.remove(path / filename)

def load_catch(pokemons):
    """
    This function randomizes 6 pokemons to catch
    """
    catch_ids = set()
    while (len(catch_ids) < 6):
        catch_ids.add(random.randint(1, 151))
    return [pokemons[repr(id)] for id in catch_ids]

def save_pokemon(poke_json):
    """
    This function saves the pokemon to the pokebelt
    """
    path = Path('pokedata/pokebelt')
    filename = path / f"{poke_json['name']}.json"
    with open(filename, 'w') as file:
        json.dump(poke_json, file)

def load_pokemon():
    """
    This function loads the pokemon from the pokebelt
    """
    jsons = list()
    path = Path('pokedata/pokebelt')
    for filename in os.listdir(path):
        with open(path/filename, 'r') as file:
            jsons += [json.load(file)]
    return jsons