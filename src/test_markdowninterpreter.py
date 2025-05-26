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
        self.assertListEqual([("image", "https://www.google.com")])

if __name__ == "__main__":
    unittest.main()