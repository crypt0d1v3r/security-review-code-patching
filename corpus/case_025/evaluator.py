import unittest
import tempfile
from pathlib import Path
import module as m

class Behavior(unittest.TestCase):
    def test_security(self):
        self.assertFalse(m.valid_count(True))

    def test_legitimate(self):
        self.assertTrue(m.valid_count(5))
        self.assertFalse(m.valid_count('5'))

if __name__ == '__main__':
    unittest.main()
