from models.code import plus
import unittest

class TestCacl(unittest.TestCase):
    def test_plus(self):
        self.assert plus(10, 10) == 21
