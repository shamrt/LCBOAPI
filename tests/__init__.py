# -*- coding: utf-8 -*-
import sys
from os import environ
from urllib.error import HTTPError

import pytest

from lcboapi import LCBOAPI


if 'LCBOAPI_ACCESS_KEY' in environ:
    access_key = environ['LCBOAPI_ACCESS_KEY']
else:
    sys.exit("No environment variable 'LCBOAPI_ACCESS_KEY' set.")
api = LCBOAPI(access_key)

VALID_STORE = {'id': 10, 'name': 'Yonge & Summerhill'}
VALID_PRODUCT = {'id': 6445, 'name': 'Creemore Springs Premium Lager'}
INVALID_STORE_ID = 1000
INVALID_PRODUCT_ID = 123456789
