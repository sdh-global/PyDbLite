__all__ = ["test_pydblite", "test_pydblite_sqlite"]

import unittest

from .test_pydblite import PyDbLiteTestCase
from .test_pydblite_sqlite import TestSQLiteFunctions, SQLiteTestCase

suite = unittest.TestSuite()
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(PyDbLiteTestCase))
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestSQLiteFunctions))
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(SQLiteTestCase))

unittest.TextTestRunner().run(suite)