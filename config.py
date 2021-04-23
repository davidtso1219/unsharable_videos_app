""" Configuration settings are defined as class variables inside
the Config class.
"""
import os

class Config(object):
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')