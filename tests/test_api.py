import unittest
import json

from game_star_wars import manager


class BaseTestCase(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        self.app = manager.app.test_client()
        manager.db.create_all()

    # executed after each test
    def tearDown(self):
        manager.db.session.rollback()
        manager.db.drop_all()


class TestAPI(BaseTestCase):

    def _add_planet(self, name=None):
        planet = manager.Planet(
            name=name or 'Tatooine',
            climate='arid',
            terrain='desert'
        )
        manager.db.session.add(planet)
        manager.db.session.commit()
        return planet

    def test_post_planet_returns_planet_data(self):
        data = {
            'name': 'Tatooine',
            'climate': 'arid',
            'terrain': 'desert',
        }
        result = self.app.post(
            '/api/planet',
            data=json.dumps(data),
            content_type='application/json'
        )
        json_data = json.loads(result.data)
        expected = {
            'id': 1,
            'name': 'Tatooine',
            'climate': 'arid',
            'terrain': 'desert',
            'number_of_movie_appearances': 5,
        }

        assert json_data == expected

    def test_get_planet_returns_paginated_planet_list(self):
        self._add_planet()

        result = self.app.get('/api/planet')
        json_data = json.loads(result.data)
        expected = {
            'num_results': 1,
            'objects': [
                {
                    'climate': 'arid',
                    'id': 1,
                    'name': 'Tatooine',
                    'number_of_movie_appearances': 5,
                    'terrain': 'desert'
                }
            ],
            'page': 1,
            'total_pages': 1
        }

        assert json_data == expected

    def test_get_planet_by_name_returns_paginated_planet_list(self):
        self._add_planet()
        self._add_planet(name='Alderaan')
        filters = [dict(name='name', op='like', val='Alderaan')]
        result = self.app.get(
            '/api/planet?q={"filters":[{"name":"name","op":"like","val":"Alderaan"}]}',
            content_type='application/json'
        )
        json_data = json.loads(result.data)
        expected = {
            'num_results': 1,
            'objects': [
                {
                    'climate': 'arid',
                    'id': 2,
                    'name': 'Alderaan',
                    'number_of_movie_appearances': 2,
                    'terrain': 'desert'
                },
            ],
            'page': 1,
            'total_pages': 1
        }

        assert json_data == expected

    def test_get_planet_by_id_returns_planet(self):
        self._add_planet()

        result = self.app.get('/api/planet/1')
        json_data = json.loads(result.data)
        expected = {
            'climate': 'arid',
            'id': 1,
            'name': 'Tatooine',
            'number_of_movie_appearances': 5,
            'terrain': 'desert'
        }

        assert json_data == expected

    def test_delete_planet_by_id_deletes_planet(self):
        self._add_planet()

        result = self.app.delete('/api/planet/1')

        assert manager.db.session.query(
            manager.Planet.query.exists()
        ).scalar() == False

    def test_patch_planet_by_id_updates_planet(self):
        self._add_planet()

        result = self.app.patch(
            '/api/planet/1',
            data=json.dumps({'climate': 'another'}),
            content_type='application/json'
        )
        json_result = json.loads(result.data)
        expected = {
            'id': 1,
            'climate': 'another',
            'name': 'Tatooine',
            'number_of_movie_appearances': 5,
            'terrain': 'desert',
        }

        assert json_result == expected
