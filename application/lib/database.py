from __future__ import absolute_import

try:
    from oursql import connect

    from application.lib.configuration import config
   
 
    connection = connect(**config.get('database'))
except ImportError:
    connection = None

