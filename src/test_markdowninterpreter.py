import unittest

from textnode import TextNode, TextType
from markdowninterpreter import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link

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
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_link_first(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) This is text with an image first",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" This is text with an image first", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links_link_first(self):
        node = TextNode(
            "[link](https://i.imgur.com/zjjcJKZ.png) This is text with a link first",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" This is text with a link first", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_with_weblink(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a web [link](https://www.google.com) as well",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a web [link](https://www.google.com) as well", TextType.TEXT)
            ],
            new_nodes
        )

    def test_split_link_with_imagelink(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a web [link](https://www.google.com) as well",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a web ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com"),
                TextNode(" as well", TextType.TEXT)
            ],
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()    