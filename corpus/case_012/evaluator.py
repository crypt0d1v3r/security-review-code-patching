import unittest
import tempfile
from pathlib import Path
import module as m

class Behavior(unittest.TestCase):
    def test_security(self):
        self.assertFalse(m.may_update({'id': 4, 'valid': False}, {'author': 4}))

    def test_legitimate(self):
        self.assertTrue(m.may_update({'id': 4, 'valid': True}, {'author': 4}))

if __name__ == '__main__':
    unittest.main()
