import unittest
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_multiple_children(self):
        children = [
            LeafNode("b", "Bold"),
            LeafNode(None, "Normal"),
            LeafNode("i", "Italic")
        ]
        parent_node = ParentNode("p", children)
        self.assertEqual(parent_node.to_html(), "<p><b>Bold</b>Normal<i>Italic</i></p>")

    def test_missing_tag_raises(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "hi")])

    def test_missing_children_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    def test_props_rendered_correctly(self):
        node = ParentNode("section", [LeafNode(None, "content")], {"class": "main", "id": "s1"})
        self.assertEqual(node.to_html(), '<section class="main" id="s1">content</section>')


if __name__ == "__main__":
    unittest.main()

