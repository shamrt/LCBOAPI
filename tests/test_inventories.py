# -*- coding: utf-8 -*-
from tests import *


def test_inventories_without_args():
    resp = api.inventories()
    assert resp['status'] == 200
    assert 'result' in resp

    res = resp['result']
    assert isinstance(res, list)
    assert len(res) == resp['pager']['records_per_page']


def test_inventories_with_store_id():
    resp = api.inventories(VALID_STORE['id'])
    assert resp['status'] == 200
    assert 'pager' in resp
    assert 'result' in resp

    assert 'store' in resp
    store = resp['store']
    assert store['id'] == VALID_STORE['id']
    assert store['name'] == VALID_STORE['name']

    res = resp['result']
    assert len(res) == resp['pager']['records_per_page']


def test_inventories_with_store_id_and_product_id():
    resp = api.inventories(VALID_STORE['id'], VALID_PRODUCT['id'])
    assert resp['status'] == 200
    assert 'pager' not in resp
    assert 'result' in resp


def test_inventories_with_params():
    per_page = 100
    resp = api.inventories(per_page=per_page)
    assert resp['status'] == 200
    assert 'pager' in resp
    assert resp['pager']['records_per_page'] == per_page
    assert 'result' in resp
    assert len(resp['result']) == per_page


def test_inventories_with_invalid_store_id():
    with pytest.raises(HTTPError):
        resp = api.inventories(store_id=INVALID_STORE_ID)


def test_inventories_with_invalid_product_id():
    with pytest.raises(HTTPError):
        resp = api.inventories(product_id=INVALID_PRODUCT_ID)


def test_inventories_with_store_id_and_invalid_product_id():
    with pytest.raises(HTTPError):
        resp = api.inventories(VALID_STORE['id'], INVALID_PRODUCT_ID)


def test_inventories_with_invalid_store_id_and_valid_product_id():
    with pytest.raises(HTTPError):
        resp = api.inventories(INVALID_STORE_ID, VALID_PRODUCT['id'])
