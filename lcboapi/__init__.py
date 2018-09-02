"""
LCBOAPI
~~~~~~~

Python wrapper for the unofficial LCBO API - https://lcboapi.com/docs
"""
import json
import time
import urllib.request
import urllib.parse
import logging
from urllib.error import URLError, HTTPError

__title__ = 'lcboapi'
__version__ = '0.2.1'
__author__ = 'Shane Martin'
__license__ = 'MIT'

BASEURL = 'https://lcboapi.com'
DATASETS_PATH = 'datasets'

logger = logging.getLogger(__name__)


class LCBOAPI(object):
    """Make LCBO API queries.

    Arguments:
        access_key = LCBO API access key
    """

    def __init__(self, access_key):
        self.access_key = access_key
        self.timeout = 0.05

    def generate_api_request(self, path, params=None):
        """Build query URL and generate LCBOAPI request object.

        Arguments:
            path = The URL path, which must always begin with the request
                endpoint ('stores', 'products', 'inventories', 'datasets')
            params = Query parametres (optional; see https://lcboapi.com/docs
                for details)

        Returns:
            Request object for LCBOAPI
        """
        url_parts = [BASEURL]
        url_parts.append(path)
        if params:
            url_params = urllib.parse.urlencode(params)
            url_parts.append('?' + url_params)
        query_url = '/'.join(url_parts)

        logger.debug('Query URL: {}'.format(query_url))

        request = urllib.request.Request(query_url)
        request.add_header(
            'Authorization', 'Token {}'.format(self.access_key))

        return request

    def __get_json(self, path, params=None):
        """Get JSON response from LCBOAPI.

        Arguments:
            path = The URL path, which must always begin with the request
                endpoint ('stores', 'products', 'inventories', 'datasets')
            params = Query parametres (optional; see https://lcboapi.com/docs
                for details)

        Returns:
            Deserialized JSON query response as Python object
        """
        request = self.generate_api_request(path, params)
        payload = urllib.request.urlopen(request)

        response = None
        try:
            response = json.load(payload)
        except ValueError:
            logger.exception("Issue with JSON payload: \"{}\"".format(payload))

        # be nice to LCBOAPI and they'll be nice to you!
        time.sleep(self.timeout)

        return response

    def stores(self, store_id=None, **params):
        """Get stores data.

        Arguments:
            store_id = LCBO store ID
            params = Query parametres (optional; see https://lcboapi.com/docs
                for details)
        """
        path = 'stores'
        if store_id:
            path = '/'.join([path, str(store_id)])
        return self.__get_json(path, params)

    def products(self, product_id=None, **params):
        """Get products data.

        Arguments:
            product_id = LCBO product ID
            params = Query parametres (optional; see https://lcboapi.com/docs
                for details)
        """
        path = 'products'
        if product_id:
            path = '/'.join([path, str(product_id)])
        return self.__get_json(path, params)

    def inventories(self, store_id=None, product_id=None, **params):
        """Get data about the presence of a product at an LCBO store.

        Arguments:
            store_id = LCBO store ID
            product_id = LCBO product ID
            params = Query parametres (optional; see https://lcboapi.com/docs
                for details)
        """
        path = 'inventories'
        if store_id and product_id:
            path = 'stores/{}/products/{}/inventory'.format(
                store_id, product_id)
        elif store_id:
            params['store_id'] = store_id
        elif product_id:
            params['store_id'] = product_id
        return self.__get_json(path, params)

    def datasets(self, dataset_id=None, **params):
        """Get a list of inventories that can be filtered and ordered by parameters.

        Arguments:
            dataset_id = An inventory ID for the specified dataset
            params = Query parametres (optional; see https://lcboapi.com/docs
                for details)
        """
        path = DATASETS_PATH
        if dataset_id:
            path = '/'.join([path, str(dataset_id)])
        return self.__get_json(path, params)

    def __get_zip(self, path):
        """Get ZIP response binary object from LCBOAPI.

        Arguments:
            dataset_id = An inventory ID for the specified dataset
        """
        zip_path = '{}.zip'.format(path)

        url_joined = urllib.parse.urljoin(BASEURL, zip_path)
        query_url = urllib.parse.urljoin(url_joined, '?access_key={}'.format(self.access_key))

        request = urllib.request.Request(query_url)

        return urllib.request.urlopen(request)

    def datasets_zip(self, dataset_id="latest"):
        """Get a ZIP of the given dataset_id.

        Arguments:
            dataset_id = An inventory ID for the specified dataset
        """
        path = '/'.join([DATASETS_PATH, str(dataset_id)])
        return self.__get_zip(path)
