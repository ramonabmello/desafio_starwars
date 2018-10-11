from .models import Planet

from marshmallow import Schema, fields


class PlanetSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    climate = fields.Str()
    terrain = fields.Str()
    number_of_movie_appearances = fields.Int()

    def make_object(self, data):
        return Planet(**data)


planet_schema = PlanetSchema()


def planet_serializer(instance):
    return planet_schema.dump(instance).data


def planet_deserializer(instance):
    return planet_schema.make_object(
        planet_schema.load(instance).data
    )
