import unittest

from textnode import TextNode, TextType
from markdowninterpreter import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestMarkDownInterpreter(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.google.com)"
        )
        self.assertListEqual([("link", "https://www.google.com")], matches)

    def test_extract_markdown_images_multi(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://www.google.com) \
             and another one ![image2](https://www.duckduckgo.com)"
        )
        self.assertListEqual([("image", "https://www.google.com"),
                              ("image2", "https://www.duckduckgo.com")],
                              matches)

    def test_extract_markdown_link_multi(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.google.com) \
            and another one [link2](https://www.duckduckgo.com)"
        )
        self.assertListEqual([("link", "https://www.google.com"), ("link2", "https://www.duckduckgo.com")],
                            matches)

if __name__ == "__main__":
    unittest.main()