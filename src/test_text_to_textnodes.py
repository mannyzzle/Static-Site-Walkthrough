import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):

    def test_mixed_markdown(self):
        raw = ("This is **text** with an _italic_ word and a `code block` "
               "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
               "and a [link](https://boot.dev)")
        result = text_to_textnodes(raw)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE,
                     "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertListEqual(expected, result)

    def test_plain_text(self):
        raw = "Nothing special here."
        self.assertListEqual(
            [TextNode(raw, TextType.TEXT)],
            text_to_textnodes(raw)
        )

    def test_only_images_and_links(self):
        raw = "![img](https://a.com) and [boot](https://boot.dev)"
        result = text_to_textnodes(raw)
        self.assertListEqual(
            [
                TextNode("img", TextType.IMAGE, "https://a.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("boot", TextType.LINK, "https://boot.dev"),
            ],
            result,
        )
if __name__ == "__main__":
    unittest.main()
