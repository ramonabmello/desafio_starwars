import flask_restless

from .app import app
from .models import Planet, db
from .serializers import planet_serializer, planet_deserializer

# Create the Flask-Restless API manager.
manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

# Create the database tables.
db.create_all()

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(
    Planet,
    methods=['GET', 'POST', 'DELETE', 'PATCH'],
    serializer=planet_serializer,
    deserializer=planet_deserializer,
    include_methods=['number_of_movie_appearances']
)
