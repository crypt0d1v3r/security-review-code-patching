import unittest
import tempfile
from pathlib import Path
import module as m

class Behavior(unittest.TestCase):
    def test_security(self):
        self.assertFalse(m.can_manage({'role': 'admin', 'tenant': 'A'}, {'tenant': 'B'}))

    def test_legitimate(self):
        self.assertTrue(m.can_manage({'role': 'admin', 'tenant': 'A'}, {'tenant': 'A'}))

if __name__ == '__main__':
    unittest.main()
