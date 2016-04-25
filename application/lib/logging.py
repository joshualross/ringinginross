from __future__ import absolute_import

import logging.config

from application.lib.configuration import config


logging.config.dictConfig(config.get('logging'))
Logger = logging.getLogger('application')  # will use the root logger
