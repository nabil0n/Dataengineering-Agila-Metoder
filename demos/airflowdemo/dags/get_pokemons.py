"""
## Test DAG for exercise 2, catching pokemons.
"""

from airflow import Dataset
from airflow.decorators import dag, task
from pendulum import datetime
import requests
import pandas as pd

@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "Astro", "retries": 3},
    tags=["example"],
)
def pokemons():
    @task(
        outlets=[Dataset("current_pokemons")]
    )
    def get_pokemons(**context) -> list[dict]:
        """
        This task gets the list of astronauts currently in space
        """
        pokemons = pd.read_html(
            "https://sv.wikipedia.org/wiki/Lista_%C3%B6ver_Pok%C3%A9mon")[1]
        namn = pokemons['Engelskt namn']
        
        for r in pokemons.iterrows():
            context["ti"].xcom_push(
                key=r.iloc["Nationellt Pokédex №"], value=r['Engelskt namn']
            )
        return namn

    # @task(
    #     outlets=[Dataset("current_pokemons")]
    # )
    # def catch_pokemon(pokemon_name = None, pokemon_idx = None) -> None:
    #     """
    #     This task catches a pokemon
    #     """
    #     idx = pokemon_idx
    #     name = pokemon_name
        
    #     print(f"Catching {name} with index {idx}")
        
    # for r in get_pokemons():
    #     catch_pokemon(pokemon_name=r['Engelskt namn'], pokemon_idx=r["Nationellt Pokédex №"])

pokemons()
