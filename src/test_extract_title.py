import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_first_h1_wins(self):
        md = "# First\n## Sub\n# Second"
        self.assertEqual(extract_title(md), "First")

    def test_missing(self):
        with self.assertRaises(ValueError):
            extract_title("No heading here")
