import unittest
from block_types import (
    block_to_block_type, BlockType
)

class TestBlockToBlockType(unittest.TestCase):

    def test_heading_levels(self):
        for hashes in range(1, 7):
            blk = "#"*hashes + " Heading"
            self.assertEqual(block_to_block_type(blk), BlockType.HEADING)

    def test_code_block(self):
        blk = "```\nprint('hi')\n```"
        self.assertEqual(block_to_block_type(blk), BlockType.CODE)

    def test_quote_block(self):
        blk = "> first line\n> second line"
        self.assertEqual(block_to_block_type(blk), BlockType.QUOTE)

    def test_unordered_list(self):
        blk = "- a\n- b\n- c"
        self.assertEqual(block_to_block_type(blk), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        blk = "1. one\n2. two\n3. three"
        self.assertEqual(block_to_block_type(blk), BlockType.ORDERED_LIST)

    def test_bad_ordered_list_returns_paragraph(self):
        blk = "1. one\n3. three"
        self.assertEqual(block_to_block_type(blk), BlockType.PARAGRAPH)

    def test_paragraph_fallback(self):
        blk = "Just a plain paragraph\nwith two lines of text."
        self.assertEqual(block_to_block_type(blk), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
