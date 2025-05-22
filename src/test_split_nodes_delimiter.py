import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_single_code_delimiter(self):
        node = TextNode("Some `code` here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Some ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " here")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_multiple_code_blocks(self):
        node = TextNode("`one` and `two`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].text, "")
        self.assertEqual(result[1].text, "one")
        self.assertEqual(result[2].text, " and ")
        self.assertEqual(result[3].text, "two")
        self.assertEqual(result[4].text, "")

    def test_uneven_delimiters(self):
        node = TextNode("Some `code is broken", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "Some `code is broken")
        self.assertEqual(result[0].text_type, TextType.TEXT)

    def test_non_text_type_skipped(self):
        node = TextNode("Should skip", TextType.BOLD)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], node)

    def test_bold_delimiter(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[1].text, "bold")

    def test_italic_delimiter(self):
        node = TextNode("It _really_ is", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text_type, TextType.ITALIC)
        self.assertEqual(result[1].text, "really")

if __name__ == "__main__":
    unittest.main()
