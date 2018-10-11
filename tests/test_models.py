import unittest
from game_star_wars import models


class TestPlanet(unittest.TestCase):
    def test_has_id(self):
        planet = models.Planet(id=1)
        assert planet.id == 1

    def test_has_name(self):
        planet = models.Planet(name='Tatooine')
        assert planet.name == 'Tatooine'

    def test_has_climate(self):
        planet = models.Planet(climate='arid')
        assert planet.climate == 'arid'

    def test_has_terrain(self):
        planet = models.Planet(terrain='desert')
        assert planet.terrain == 'desert'

    def test_representation(self):
        planet = models.Planet(
            id=1,
            name='Tatooine',
            climate='arid',
            terrain='desert'
        )
        expected = 'Planet: Tatooine\nClimate: arid\nTerrain: desert'

        assert repr(planet) == expected

    def test_number_of_movie_appearances(self):
        planet = models.Planet(name='Tatooine')
        assert planet.number_of_movie_appearances == 5
