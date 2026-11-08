import unittest
import tempfile
from pathlib import Path
import module as m

class Behavior(unittest.TestCase):
    def test_security(self):
        self.assertFalse(m.can_access({'id': 4, 'account': 'A'}, {'author': 4, 'account': 'B'}))

    def test_legitimate(self):
        self.assertTrue(m.can_access({'id': 4, 'account': 'A'}, {'author': 4, 'account': 'A'}))

if __name__ == '__main__':
    unittest.main()
