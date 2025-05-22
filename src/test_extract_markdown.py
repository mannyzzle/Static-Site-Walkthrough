import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_multiple_images(self):
        text = "Check ![a](https://a.com) and ![b](https://b.com)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [("a", "https://a.com"), ("b", "https://b.com")],
            matches
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is [Google](https://google.com) and [YouTube](https://youtube.com)"
        )
        self.assertListEqual(
            [("Google", "https://google.com"), ("YouTube", "https://youtube.com")],
            matches
        )

    def test_no_false_positive_on_images(self):
        matches = extract_markdown_links(
            "This is ![not a link](https://image.com)"
        )
        self.assertEqual(matches, [])

    def test_no_matches(self):
        text = "This is plain text with no markdown."
        self.assertEqual(extract_markdown_images(text), [])
        self.assertEqual(extract_markdown_links(text), [])

if __name__ == "__main__":
    unittest.main()
