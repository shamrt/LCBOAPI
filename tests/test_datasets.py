import pytest
from pytest_mock import mocker
import urllib

from zipfile import ZipFile
from io import BytesIO

from tests import api
from lcboapi import LCBOAPI


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


def _check_result_attrs(result_set):
    for attr in RESULT_ATTRIBUTES:
        assert attr in result_set


def test_datasets_without_args():
    resp = api.datasets()
    assert resp['status'] == 200
    assert 'pager' in resp
    assert 'result' in resp

    for res in resp['result']:
        _check_result_attrs(res)


@pytest.mark.parametrize("test_input", [
    "latest",
    DATASET_ID,
])
def test_datasets_with_dataset_id(test_input):
    resp = api.datasets(test_input)
    assert resp['status'] == 200
    assert 'pager' not in resp
    assert 'result' in resp
    _check_result_attrs(resp['result'])


@pytest.mark.parametrize("test_input", [
    "latest",
])
def test_datasets_zip_with_dataset_id_returns_expected_files(test_input):
    resp = api.datasets_zip(test_input)
    zipfile = ZipFile(BytesIO(resp.read()))

    assert zipfile.namelist() == ['stores.csv', 'products.csv', 'inventories.csv']
