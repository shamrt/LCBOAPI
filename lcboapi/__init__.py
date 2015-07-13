# -*- coding: utf-8 -*-
"""
LCBOAPI
~~~~~~~

Python wrapper for the unofficial LCBO API - https://lcboapi.com/docs
"""

__title__ = 'lcboapi'
__version__ = '0.1.1'
__author__ = 'Shane Martin'
__license__ = 'MIT'

import json
import time
import urllib
import urllib2
import logging as log


class LCBOAPI(object):
    """Make LCBO API queries.

    Arguments:
        access_key = LCBO API access key
    """
    def __init__(self, access_key):
        self.access_key = access_key
        self.response_type = 'json'
        self.timeout = 0.05
        self.url = 'https://lcboapi.com'

    def set_response_type(self, response_type):
        """Set response format for the API (default = JSON).

        Arguments:
            response_type = The default response format for the API ('json' or 'csv')
        """
        if response_type == 'json' or response_type == 'csv':
            self.response_type = response_type

    def _make_query(self, path, params=None):
        """Build query URL and make request.

        Arguments:
            path = The URL path, which must always begin with the request endpoint
                ('stores', 'products', 'inventories', 'datasets')
            params = Query parametres (optional; see https://lcboapi.com/docs for details)

        Returns:
            Deserialized JSON query response as Python object
        """
        url_parts = [self.url]
        url_parts.append(path)
        if params:
            url_params = urllib.urlencode(params)
            url_parts.append('?' + url_params)
        query_url = '/'.join(url_parts)

        log.debug('Query URL: {}'.format(query_url))

        request = urllib2.Request(query_url)
        request.add_header('Authorization', 'Token {}'.format(self.access_key))

        response = json.load(urllib2.urlopen(request))

        time.sleep(self.timeout)  # be nice to LCBOAPI and they'll be nice to you!

        return response

    def stores(self, store_id=None, **params):
        """Get stores data.

        Arguments:
            store_id = LCBO store ID
            params = Query parametres (optional; see https://lcboapi.com/docs for details)
        """
        path = 'stores'
        if store_id:
            path = '/'.join([path, str(store_id)])
        return self._make_query(path, params)

    def products(self, product_id=None, **params):
        """Get products data.

        Arguments:
            product_id = LCBO product ID
            params = Query parametres (optional; see https://lcboapi.com/docs for details)
        """
        path = 'products'
        if product_id:
            path = '/'.join([path, str(product_id)])
        return self._make_query(path, params)


    def inventories(self, store_id=None, product_id=None, **params):
        """Get data about the presence of a product at an LCBO store.

        Arguments:
            store_id = LCBO store ID
            product_id = LCBO product ID
            params = Query parametres (optional; see https://lcboapi.com/docs for details)
        """
        path = 'inventories'
        if store_id and product_id:
            path = 'stores/{}/products/{}/inventory'.format(store_id, product_id)
        elif store_id:
            params['store_id'] = store_id
        elif product_id:
            params['store_id'] = product_id
        return self._make_query(path, params)


    def datasets(self, dataset_id=None, **params):
        """Get a list of inventories that can be filtered and ordered by parameters.

        Arguments:
            dataset_id = An inventory ID for the specified dataset
            params = Query parametres (optional; see https://lcboapi.com/docs for details)
        """
        path = 'datasets'
        if dataset_id:
            path = '/'.join([path, str(dataset_id)])
        return self._make_query(path, params)
