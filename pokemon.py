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


def get_amount_of_pokemons_same_gen(name: str) -> int:
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


def get_evolution_line(name: str) -> list:
    """Returns the list of the evolution line for the given pokemon name.

    Args:
        name (str): The name of pokemon to be searched.

    Returns:
        list: The list of pokemon names in the evolution line for the given pokemon name.
    """
    r = requests.get(f"https://pokeapi.glitch.me/v1/pokemon/{name}")
    family = r.json()[0]["family"]
    evolution_line = family["evolutionLine"]
    return evolution_line
