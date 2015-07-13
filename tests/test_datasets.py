# -*- coding: utf-8 -*-
from tests import *


RESULT_ATTRIBUTES = [
    'id',
    'total_products',
    'total_stores',
    'total_inventories',
    'total_product_inventory_count',
    'total_product_inventory_volume_in_milliliters',
    'total_product_inventory_price_in_cents',
    'store_ids',
    'product_ids',
    'added_product_ids',
    'removed_product_ids',
    'removed_product_ids',
    'removed_store_ids',
    'removed_store_ids',
    'csv_dump',
    'created_at',
    'updated_at',

]
DATASET_ID = 800


def test_datasets_without_args():
    resp = api.datasets()
    assert resp['status'] == 200
    assert 'pager' in resp

    assert 'result' in resp
    res = resp['result']
    for attr in RESULT_ATTRIBUTES:
        assert attr in res[0]


def test_datasets_with_dataset_id():
    resp = api.datasets(DATASET_ID)
    assert resp['status'] == 200
    assert 'pager' not in resp

    assert 'result' in resp
    for attr in RESULT_ATTRIBUTES:
        assert attr in resp['result']
