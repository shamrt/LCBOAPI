import sys
from os import environ
from lcboapi import LCBOAPI


if 'LCBOAPI_ACCESS_KEY' in environ:
    access_key = environ['LCBOAPI_ACCESS_KEY']
else:
    sys.exit("No environment variable 'LCBOAPI_ACCESS_KEY' set.")

api = LCBOAPI(access_key)
