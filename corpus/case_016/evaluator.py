import unittest
import tempfile
from pathlib import Path
import module as m

class Behavior(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        p = Path(self.tmp.name)
        self.root = p / 'root'
        self.root.mkdir()
        (self.root / 'ok.txt').write_text('hello')
        (p / 'secret.txt').write_text('secret')
        (self.root / 'config.key').write_text('key')
        (self.root / 'link.txt').symlink_to(p / 'secret.txt')

    def tearDown(self):
        self.tmp.cleanup()

    def test_security(self):
        with self.assertRaises((ValueError, PermissionError, FileNotFoundError)):
            m.read_attachment(self.root, '../secret.txt')

    def test_legitimate(self):
        self.assertEqual(m.read_attachment(self.root, 'ok.txt'), 'hello')

if __name__ == '__main__':
    unittest.main()
