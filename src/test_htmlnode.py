import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode(props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertIn('href="https://example.com"', result)
        self.assertIn('target="_blank"', result)
        self.assertTrue(result.startswith(" "))

    def test_props_to_html_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode(tag="a", value="Click me", children=None, props={"href": "https://example.com"})
        repr_str = repr(node)
        self.assertIn("tag=a", repr_str)
        self.assertIn("value=Click me", repr_str)
        self.assertIn("props={'href': 'https://example.com'}", repr_str)




if __name__ == "__main__":
    unittest.main()
