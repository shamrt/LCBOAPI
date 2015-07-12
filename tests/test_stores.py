from os import environ

import pytest

from lcboapi import LCBOAPI

access_key = environ['LCBOAPI_ACCESS_KEY']
api = LCBOAPI(access_key)

def test_stores_without_args():
    resp = api.stores()
    assert resp['status'] == 200
    assert 'result' in resp
    assert isinstance(resp['result'], list)
    assert len(resp['result']) > 0

    first_result = resp['result'][0]
    assert 'id' in first_result
    assert 'inventory_count' in first_result


def test_stores_with_store_id():
    resp = api.stores(10)
    assert resp['status'] == 200
    assert 'pager' not in resp
    assert 'result' in resp

    res = resp['result']
    assert res['id'] == '10'
    assert res['name'] == 'Yonge & Summerhill'


def test_stores_with_invalid_store_id():
    resp = api.stores(1000)
    assert resp['status'] == 404
    assert resp['message'] != None
    assert resp['result'] == None
