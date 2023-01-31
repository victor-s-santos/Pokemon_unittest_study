import unittest
from pokemon import (
    get_pokemon_types,
    get_evolution_line,
    get_amount_of_pokemons_same_gen,
)


class TestPokemon(unittest.TestCase):
    def setUp(self):
        self.pikachu = "pikachu"
        self.expected_list_types = [
            "Bug",
            "Dark",
            "Dragon",
            "Electric",
            "Fairy",
            "Fighting",
            "Fire",
            "Flying",
            "Ghost",
            "Grass",
            "Ground",
            "Ice",
            "Normal",
            "Poison",
            "Psychic",
            "Rock",
            "Steel",
            "Water",
        ]

    def test_get_pokemon_types_format(self):
        """Must return a list instance."""
        list_types = get_pokemon_types(self.pikachu)
        self.assertIsInstance(list_types, list)


if __name__ == "__main__":
    unittest.main()
