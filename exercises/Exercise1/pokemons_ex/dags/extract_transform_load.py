from airflow import DAG
from airflow.decorators import task
from pendulum import datetime
import pandas as pd
import requests
import include.utils as utils

with DAG(
    dag_id="etl_pokemon",
    start_date=datetime(2024, 1, 1),
    schedule="*/1 * * * *",
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "Astro", "retries": 1},
):
    @task
    def extract_pokemons(**context):
        """
        This task extracts the list of the 151 first pokemons from the wiki using pandas
        """
        poke_html = pd.read_html(
            "https://sv.wikipedia.org/wiki/Lista_%C3%B6ver_Pok%C3%A9mon")[1][:151]
        
        pokemons = {id: name for (id, name) in zip(poke_html["Nationellt Pokédex №"],
                                                    poke_html["Engelskt namn"])}
        return pokemons
    
    @task
    def transform_load_pokemons(pokemons):
        utils.clear_pokebelt()
        for pokemon in utils.load_catch(pokemons):
            pokemon_json = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon.lower()}").json()
            utils.save_pokemon(pokemon_json)
    
    @task
    def print_pokemon():
        for pokemon in utils.load_pokemon():
            print(f"Pokemon {pokemon['name']} has the id {pokemon['id']} and has base happiness {pokemon['base_happiness']}")
    
    transform_load_pokemons(extract_pokemons()) >> print_pokemon()