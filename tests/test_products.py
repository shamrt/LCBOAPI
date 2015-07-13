# -*- coding: utf-8 -*-
from tests import *


def test_products_without_args():
    resp = api.products()
    assert resp['status'] == 200
    assert 'result' in resp
    assert isinstance(resp['result'], list)
    assert len(resp['result']) > 0

    first_result = resp['result'][0]
    assert 'id' in first_result
    assert 'inventory_count' in first_result


def test_products_with_product_id():
    product_id = 688135
    resp = api.products(product_id)
    assert resp['status'] == 200
    assert 'pager' not in resp
    assert 'result' in resp

    res = resp['result']
    assert res['product_no'] == product_id
    assert res['name'] == 'Molson Canadian'


def test_products_with_invalid_product_id():
    with pytest.raises(HTTPError):
        resp = api.products(10000000)


def test_products_with_params():
    resp = api.products(per_page=100)
    assert resp['status'] == 200
    assert 'pager' in resp
    assert resp['pager']['records_per_page'] == 100
    assert 'result' in resp
    assert len(resp['result']) == 100
