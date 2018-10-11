from .db import db

import requests


# Create your Flask-SQLAlchemy models as usual but with the following two
# (reasonable) restrictions:
#    1. They must have an id column of type Integer.
#    2. They must have an __init__ method which accepts keyword arguments for
#       all columns (the constructor in flask.ext.sqlalchemy.SQLAlchemy.Model
#       suplies such a method, so you don't need to declare a new one).
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    climate = db.Column(db.String(50))
    terrain = db.Column(db.String(50))

    @property
    def number_of_movie_appearances(self):
        result = requests.get(
            f'https://swapi.co/api/planets/?search={self.name}'
        ).json()
        if result['count'] > 0:
            return len(result['results'][0]['films'])

        return 0

    def __repr__(self):
        return f'Planet: {self.name}\nClimate: {self.climate}\nTerrain: {self.terrain}'
