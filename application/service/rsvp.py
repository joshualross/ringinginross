from __future__ import absolute_import

from uuid import uuid4

from application.lib.database import connection
from application.entity import GuestEntity


class RSVPService(object):

    @staticmethod
    def search_by_name(first_name, last_name):

        query = "SELECT uuid FROM guest WHERE first_name LIKE ? AND last_name LIKE ?"

        with connection as cursor:
            cursor.execute(query, ("%{}%".format(first_name), "%{}%".format(last_name)))
            row = cursor.fetchone()

        return row[0] if row else None


    @staticmethod
    def fetch(uuid):
        entity = GuestEntity()
        fields = entity.get_schema_fields()
        query = "SELECT {fields} FROM guest WHERE uuid = ?".format(
            fields=','.join(fields)
        )

        with connection as cursor:
            cursor.execute(query, (uuid,))
            row = cursor.fetchone()

        data = {}
        for key, value in enumerate(row):
            data.update({fields[key]: value})

        entity.load(data)
        return entity



    @staticmethod
    def create(self, first_name, last_name, email, primary_guest_uuid=None):
        """Create a guest as a plus 1 if primary_guest_uuid is set."""

        query = "INSERT INTO guest (uuid, first_name, last_name, email, is_allowed_guest) VALUES (?, ?, ?, ? ,?)"
        guest_uuid = str(uuid4())
        with connection as cursor:
            cursor.execute(query, (guest_uuid, first_name, last_name, email, False))

        return RSVPService.update(primary_guest_uuid, {'guest_uuid': guest_uuid})



    @staticmethod
    def update(uuid, data):

        query = "UPDATE guest SET "
        params = []
        for key, value in data:
            query += " `{}` = ?".format(key)
            params.append(value)

        with connection as cursor:
            cursor.execute(query, params)
            return cursor.rowcount
