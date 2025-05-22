import tempfile, pathlib, os, shutil, unittest
from copy_static import copy_static

class TestCopyStatic(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.static_dir = pathlib.Path(self.tmp.name) / "static"
        self.public_dir = pathlib.Path(self.tmp.name) / "public"
        # Make fake static tree
        (self.static_dir / "images").mkdir(parents=True)
        (self.static_dir / "images" / "a.png").write_text("img")
        (self.static_dir / "index.css").write_text("body{}")

    def tearDown(self):
        self.tmp.cleanup()

    def test_copy(self):
        copy_static(self.static_dir, self.public_dir)
        self.assertTrue((self.public_dir / "images" / "a.png").exists())
        self.assertTrue((self.public_dir / "index.css").exists())

if __name__ == "__main__":
    unittest.main()
