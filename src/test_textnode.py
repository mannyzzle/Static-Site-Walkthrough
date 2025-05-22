import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_equal_different_text(self):
        node1 = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("World", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_type(self):
        node1 = TextNode("Hello", TextType.BOLD)
        node2 = TextNode("Hello", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_url(self):
        node1 = TextNode("Click here", TextType.LINK, "https://example.com")
        node2 = TextNode("Click here", TextType.LINK, "https://another.com")
        self.assertNotEqual(node1, node2)

    def test_equal_with_none_url(self):
        node1 = TextNode("Plain", TextType.TEXT, None)
        node2 = TextNode("Plain", TextType.TEXT)
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
