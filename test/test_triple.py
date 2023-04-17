import unittest

from triple import triple

class TestTriple(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(6, triple(2))

    def test_negative_integer(self):
        self.assertEqual(-6, triple(-2))