from __future__ import absolute_import

from marshmallow import fields

from application.lib.entity import Entity, Schema, Timestamp as FieldTimestamp


class GuestSchema(Schema):
    uuid = fields.UUID(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(allow_none=True, missing=None, default=None)
    is_allowed_guest = fields.Int(default=False)
    guest_uuid = fields.UUID(allow_none=True, missing=None, default=None)
    message = fields.String(allow_none=True, missing=None, default=None)
    created = FieldTimestamp(required=True)
    updated = FieldTimestamp(required=True)


class GuestEntity(Entity):
    schema = GuestSchema

