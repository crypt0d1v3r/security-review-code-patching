import unittest
import tempfile
from pathlib import Path
import module as m

class Behavior(unittest.TestCase):
    def test_security(self):
        self.assertFalse(m.valid_quota(11))

    def test_legitimate(self):
        self.assertTrue(m.valid_quota(5))
        self.assertFalse(m.valid_quota(0))

if __name__ == '__main__':
    unittest.main()
