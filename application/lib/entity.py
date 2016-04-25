from __future__ import absolute_import

from abc import ABCMeta, abstractproperty
import arrow
from arrow.parser import ParserError
import marshmallow
from marshmallow import fields


class Entity(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def schema(self):
        pass

    def __init__(self, data=None, **kwargs):
        if data:
            self.load(data, **kwargs)

    def load(self, data, **kwargs):
        result = self.schema().load(data, **kwargs)

        # If the data is invalid
        if not result.data or result.errors:
            raise ValueError(
                result.errors or 'No valid data found'
            )

        for key, value in result.data.items():
            setattr(self, key, value)

    def dump(self, **kwargs):
        """Serialize an entity to python primitives."""
        result = self.schema().dump(self, **kwargs)
        if result.errors:
            raise ValueError(result.errors)

        return result.data

    def get(self, key, default=None):
        """Provide dictionary type access."""
        return getattr(self, key, default)

    @classmethod
    def get_schema_fields(cls):
        return [field for field in cls.schema._declared_fields.keys()]


class Schema(marshmallow.Schema):
    pass


class Timestamp(fields.Field):
    """A datetime represented by a unix timestamp

    Example: ``'1447588801'``

    """
    localtime = False
    default_error_messages = {
        'invalid': 'Not a valid datetime or timestamp.',
        'format': '"{input}" cannot be formatted as a timestamp.',
    }

    def _deserialize(self, value, attr, data):
        if not value:  # Falsy values, e.g. '', None, [] are not valid
            raise self.fail('invalid')
        try:
            return arrow.get(value).timestamp
        except ParserError:
            self.fail('invalid')
