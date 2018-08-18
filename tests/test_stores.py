from urllib.error import HTTPError
import pytest

from tests import api
from .constants import VALID_STORE, INVALID_STORE_ID


def test_stores_without_args():
    """Returns a list of inventories that can be filtered and ordered by parameters.
    """
    resp = api.stores()
    assert resp['status'] == 200
    assert 'result' in resp
    assert isinstance(resp['result'], list)
    assert len(resp['result']) > 0

    first_result = resp['result'][0]
    assert 'id' in first_result
    assert 'inventory_count' in first_result


def test_stores_with_store_id():
    resp = api.stores(VALID_STORE['id'])
    assert resp['status'] == 200
    assert 'pager' not in resp
    assert 'result' in resp

    res = resp['result']
    assert res['id'] == VALID_STORE['id']
    assert res['name'] == VALID_STORE['name']


def test_stores_with_invalid_store_id():
    with pytest.raises(HTTPError):
        api.stores(INVALID_STORE_ID)


def test_stores_with_params():
    per_page = 100
    resp = api.stores(per_page=per_page)
    assert resp['status'] == 200
    assert 'pager' in resp
    assert resp['pager']['records_per_page'] == per_page
    assert 'result' in resp
    assert len(resp['result']) == per_page
