import unittest
from unittest.mock import MagicMock
from pokemon import Pokemon


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
        self.pokemon = Pokemon(name=self.pikachu)

    @unittest.mock.patch(
        "pokemon.Pokemon.get_requests_pokemon_info",
        return_value=[{"name": "Pikachu", "types": ["Eletric"]}],
    )
    def test_get_pokemon_types_format(self, mocked_request: MagicMock()):
        """Must return a list instance."""
        list_types = self.pokemon.get_pokemon_types()
        self.assertIsInstance(list_types, list)

    @unittest.mock.patch(
        "pokemon.Pokemon.get_requests_pokemon_info",
        return_value=[{"name": "Pikachu", "types": ["Eletric"]}],
    )
    def test_full_return_get_pokemon_types(self, mocked_request: MagicMock()):
        list_types = self.pokemon.get_pokemon_types()
        self.assertEqual(list_types, ["Eletric"])

    @unittest.mock.patch(
        "pokemon.Pokemon.get_requests_pokemon_info",
        return_value=[{"name": "Pikachu", "gen": 1}],
    )
    @unittest.mock.patch("pokemon.Pokemon.get_number_of_gen", return_value=1)
    def test_full_return_of_get_amount_of_pokemons_same_gen(
        self, mocked_pokemon_info: MagicMock(), mocked_pokemon_count: MagicMock()
    ):
        numer_pokemons_same_gen = self.pokemon.get_amount_of_pokemons_same_gen()
        self.assertEqual(numer_pokemons_same_gen, 151)


if __name__ == "__main__":
    unittest.main()
