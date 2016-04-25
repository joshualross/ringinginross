from __future__ import absolute_import

import os

from yaml import load
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from application import BASE_DIR

config = {}
with open(BASE_DIR + '/config/base.yaml') as config_file:
    config.update(load(config_file, Loader=Loader))
