import argparse
import requests
import logging
from decouple import config
from pymongo import MongoClient

logging.basicConfig(
    format="%(asctime)s - %(pathname)s:%(lineno)d - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)


class Pokemon:
    def __init__(self, name):
        self.name = name

    def get_requests(self):
        """Realize the requests.get"""
        r = requests.get(f"https://pokeapi.glitch.me/v1/pokemon/{name}")
        return r.json()

    def get_pokemon_types(self) -> list:
        """Returns a list of types names for the given pokemon name.

        Args:
            name (str): The name of pokemon to be searched.

        Returns:
            list: A list of types names of respective pokemon
        """
        return self.get_requests()[0]["types"]

    def get_amount_of_pokemons_same_gen(self) -> int:
        """Returns the amount of pokemons in the same gen as the given pokemon name.

        Args:
            name (str): The name of pokemon to be searched.

        Returns:
            int: The amount of pokemons in the same gen.
        """
        r = requests.get(f"https://pokeapi.glitch.me/v1/pokemon/{name}")
        n_gen = r.json()[0]["gen"]

        r = requests.get(f"https://pokeapi.glitch.me/v1/pokemon/counts")
        return r.json()[f"gen{n_gen}"]

    def get_evolution_line(self) -> list:
        """Returns the list of the evolution line for the given pokemon name.

        Args:
            name (str): The name of pokemon to be searched.

        Returns:
            list: The list of pokemon names in the evolution line for the given pokemon name.
        """
        family = self.get_requests()[0]["family"]
        evolution_line = family["evolutionLine"]
        return evolution_line


def insert_pokemon_in_database(name: str) -> str:
    host = config("HOST", default="localhost")
    port = config("PORT", default="27027")
    username = config("MONGO_INITDB_ROOT_USERNAME")
    password = config("MONGO_INITDB_ROOT_PASSWORD")
    local_client = MongoClient(
        host="mongodb://localhost:27017", username="teste", password="teste"
    )
    try:
        pokemon_types = get_pokemon_types(name=name)
        dict_value = {"name": name, "types": pokemon_types}
        local_client["pokemons"]["pokemon_info"].insert_one(dict_value)
        return f"Pokemon {name} has been inserted successfully!"
    except Exception as e:
        return f"An exception has been occured: {e}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="migrate_collection_users_to_cons_consumers")
    parser.add_argument("-n", "--name", required=True, help="pokemon_name")
    args = parser.parse_args()
    logging.info(f"Inserting Pokemon {args.name} to Database...")

    try:
        insert_pokemon_in_database(name=args.name)
        logging.info(f"The Pokemon {args.name} has been inserted into database!")
    except Exception as e:
        logging.error(f"An exception has been occured: {e}")
