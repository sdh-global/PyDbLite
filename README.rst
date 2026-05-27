This is fork of https://github.com/PierreQuentel/PyDbLite

It does support Python 3.13 and latest pip



PyDbLite
=============

PyDbLite is

* a fast, pure-Python, untyped, in-memory database engine, using
  Python syntax to manage data, instead of SQL
* a pythonic interface to SQLite using the same syntax as the
  pure-Python engine for most operations (except database connection
  and table creation because of each database specificities)

PyDbLite is suitable for a small set of data where a fully fledged DB would be overkill.

Supported Python versions: 3.9+

Build status: |build-status|

Latest Pypi release: |pypi|

Read the documentation: |docs|

Installation
---------------

PIP
~~~~~~~~~

.. code-block:: bash

    pip install PyDbLite3

Manually
~~~~~~~~~

Download the source and execute

.. code-block:: bash

    pip install .

Changelog
---------------
`docs/source/changelog.rst <docs/source/changelog.rst>`_

Tests
---------------

Run tests with

.. code-block:: bash

    pytest

Run individual tests like this:

.. code-block:: bash

    pytest tests/test_pydblite.py
    pytest tests/test_pydblite_sqlite.py
    pytest tests/test_pydblite_sqlite.py -k test_filter_or

Run tests across all supported Python versions (3.9 - 3.13) with

.. code-block:: bash

    tox

Authors:
  * Pierre Quentel (pierre.quentel@gmail.com)
  * Bendik Rønning Opstad (bro.devel@gmail.com)
  * Viacheslav Vic Bukhantsov (vic.bukhantsov@gmail.com)
