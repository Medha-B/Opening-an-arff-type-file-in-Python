from models.code import plus
import unittest


class TestCode(unittest.TestCase):
    def test_plus(self):
        result = plus(10, 10)
        self.assertEqual(result, 20)
