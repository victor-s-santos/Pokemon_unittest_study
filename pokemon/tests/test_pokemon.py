import unittest
from pokemon import (
    get_pokemon_types,
    get_evolution_line,
    get_amount_of_pokemons_same_gen,
    get_evolution_line,
    insert_pokemon_in_database,
)


class TestPokemonFormat(unittest.TestCase):
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

    def test_get_amount_of_pokemons_same_gen_format(self):
        """Must return a int instance."""
        amount_of_pokemons = get_amount_of_pokemons_same_gen(self.pikachu)
        self.assertIsInstance(amount_of_pokemons, int)

    def test_get_evolution_line_format(self):
        """Must return a list instance."""
        evolution_line = get_evolution_line(self.pikachu)
        self.assertIsInstance(evolution_line, list)

    def test_insert_pokemon_in_database(self):
        """Must return a string instance."""
        insert_pokemon_in_database_obj = insert_pokemon_in_database(self.pikachu)
        self.assertIsInstance(insert_pokemon_in_database_obj, str)


if __name__ == "__main__":
    unittest.main()
