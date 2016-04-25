from __future__ import absolute_import

from oursql import connect

from application.lib.configuration import config

connection = connect(**config.get('database'))