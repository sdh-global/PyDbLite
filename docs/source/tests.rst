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
