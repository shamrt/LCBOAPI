# -*- coding: utf-8 -*-
"""
LCBOAPI
~~~~~~~

Python wrapper for the unofficial LCBO API - https://lcboapi.com/docs
"""

__title__ = 'lcboapi'
__version__ = 0.0.1
__author__ = 'Shane Martin'
__license__ = 'MIT'

import json
import time
import urllib
import urllib2
import logging as log


class Query(object):
    """Make LCBO API query.

    Arguments:
        access_key = LCBO API access key
    """
    def __init__(self, access_key):
        self.access_key = access_key
        self.response_type = 'json'
        self.timeout = 0.05
        self.url = 'https://lcboapi.com'

    def set_response_type(response_type):
        """Set response format for the API (default = JSON).

        Arguments:
            response_type = The default response format for the API ('json' or 'csv')
        """
        if response_type == 'json' or response_type == 'csv':
            self.response_type = response_type

    def _make_query(endpoint, path=None, **params):
        """Build query URL and make request.

        Arguments:
            endpoint = The request endpoint ('stores', 'products', 'inventories', 'datasets')
            path = Extra path string for the endpoint (e.g., 'store_id' for 'store' endpoint)
            params = Query parametres (see https://lcboapi.com/docs for options)

        Returns:
            Deserialized JSON query response as Python object
        """
        url = [self.url]
        url.append(endpoint)
        if path:
            url.append(path)
        params = urllib.urlencode(params)
        if params:
            url.append('?' + params)

        log.debug('Query URL: {}'.format('/'.join(url)))

        request = urllib2.Request('/'.join(url))
        request.add_header('Authorization', 'Token {}'.format(self.access_key))

        response = json.load(urllib2.urlopen(request))

        if response['status'] != 200:
            log.warn("There was a problem with the query.\nResponse {}: {}".format(
                response['status'], response['message']))

        time.sleep(self.timeout)  # be nice to LCBOAPI and they'll be nice to you!

        return response
