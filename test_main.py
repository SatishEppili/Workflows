import unittest

from main import add

class TestMain(unittest.TestCases):
    def test_add(self):
        assert(1,2) == 3
        assert(-1,1) == 0