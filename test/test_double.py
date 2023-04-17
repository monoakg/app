import unittest

from double import double

class TestDouble(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(4, double(2))

    def test_negative_integer(self):
        self.assertEqual(-4, double(-2))

    def test_float(self):
        self.assertEqual(3.5, double(1.75))