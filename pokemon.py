import requests


def get_pokemon_types(name: str) -> list:
    """Returns a list of types names for the given pokemon name.

    Args:
        name (str): The name of pokemon to be searched.

    Returns:
        list: A list of types names of respective pokemon
    """
    r = requests.get(f"https://pokeapi.glitch.me/v1/pokemon/{name}")
    return r.json()[0]["types"]
