import unittest
from textnode import TextNode, TextType
from split_nodes_media import split_nodes_image, split_nodes_link

class TestSplitNodesImageLink(unittest.TestCase):

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) "
            "and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            result,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) "
            "and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            result,
        )

    def test_image_not_split_by_link(self):
        txt = "Here is ![img](https://a.com) only."
        nodes = split_nodes_link([TextNode(txt, TextType.TEXT)])
        self.assertEqual(len(nodes), 1)          # untouched
        self.assertEqual(nodes[0].text, txt)

    def test_non_text_nodes_passthrough(self):
        bold_node = TextNode("**bold**", TextType.BOLD)
        self.assertEqual(split_nodes_image([bold_node]), [bold_node])
        self.assertEqual(split_nodes_link([bold_node]), [bold_node])

if __name__ == "__main__":
    unittest.main()
