import unittest
from markdown_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):

    def test_basic_split(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_excessive_blank_lines(self):
        md = "\n\nA\n\n\n\nB\n\n\nC\n\n"
        self.assertEqual(markdown_to_blocks(md), ["A", "B", "C"])

    def test_no_blank_lines(self):
        md = "Single block"
        self.assertEqual(markdown_to_blocks(md), ["Single block"])

if __name__ == "__main__":
    unittest.main()
