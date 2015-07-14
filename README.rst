LCBOAPI - v0.1.3
================

Python wrapper for the unofficial LCBO API

Full API documentation for LCBO API can be found at:
[https://lcboapi.com/docs\ ]

Installation
------------

Via PyPI:

::

    $ pip install lcboapi

Via Github:

::

    $ git clone https://github.com/shamrt/LCBOAPI.git
    $ cd LCBOAPI
    $ python setup.py install

Usage
-----

Obtain an `access key <https://lcboapi.com/sign-up>`__ from LCBO API.

Initialize API wrapper:

.. code:: python

    from lcboapi import LCBOAPI

    api = LCBOAPI('your_API_access_key')

Get data for store #614:

.. code:: python

    print api.stores(614)

Testing
-------

First setup your virtual environment:

::

    $ virtualenv env
    $ . env/bin/active
    $ pip install -r requirements.txt

Then set an environment variable for your API access key:

.. code:: bash

    $ export LCBOAPI_ACCESS_KEY='your_API_access_key'

Finally, run tests:

::

    $ py.test

