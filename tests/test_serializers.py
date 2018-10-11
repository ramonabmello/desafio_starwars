import unittest

from game_star_wars import models, serializers


class TestPlanetSerializers(unittest.TestCase):
    def test_planet_serializer_returns_dict_when_given_a_planet_instance(self):
        planet = models.Planet(
            id=1,
            name='Tatooine',
            climate='arid',
            terrain='desert'
        )
        expected = {
            'id': 1,
            'name': 'Tatooine',
            'climate': 'arid',
            'terrain': 'desert',
            'number_of_movie_appearances': 5,
        }

        assert serializers.planet_serializer(planet) == expected
