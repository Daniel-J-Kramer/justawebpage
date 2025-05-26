import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from markdowninterpreter import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a url node", TextType.TEXT, "https://www.boot.dev")
        node2 = TextNode("This is a url node", TextType.TEXT, "https://github.com")
        self.assertNotEqual(node, node2)

    def test_textvurl(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a url node", TextType.TEXT, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is BOLD text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is BOLD text")

    def test_italic(self):
        node = TextNode("This is Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is Italic text")

    def test_code(self):
        node = TextNode("This is Code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is Code text")
    
    def test_link(self):
        node = TextNode("This is a Link", TextType.LINK, {"href": "https://www.google.com"})
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a Link")
        self.assertEqual(html_node.props_to_html(), " href=\"https://www.google.com\"")
    
    def test_image(self):
        node = TextNode("", TextType.IMAGE, {"src": "https://www.image.com", "alt": "This is an Image"})
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props_to_html(), " src=\"https://www.image.com\" alt=\"This is an Image\"")

    def test_no_type(self):
        with self.assertRaises(Exception):
            node = TextNode("This has no type", None)
            html_node = text_node_to_html_node(node)

    def test_split_nodes_not_texttype(self):
        node = TextNode("This is BOLD text", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is BOLD text", TextType.BOLD)])

    def test_split_nodes_BOLD(self):
        node = TextNode("This is text with **bold words** inside.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with ", TextType.TEXT),
                                     TextNode("bold words", TextType.BOLD),
                                     TextNode(" inside.", TextType.TEXT)
                                    ]

                        )
    def test_split_nodes_ITALIC(self):
        node = TextNode("This is text with _italic words_ inside.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("This is text with ", TextType.TEXT),
                                     TextNode("italic words", TextType.ITALIC),
                                     TextNode(" inside.", TextType.TEXT)
                                    ]

                        )

    def test_split_nodes_CODE(self):
        node = TextNode("This is text with `code words` inside.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with ", TextType.TEXT),
                                     TextNode("code words", TextType.CODE),
                                     TextNode(" inside.", TextType.TEXT)
                                    ]

                        )

    def test_split_nodes_missing_delimiter(self):
        with self.assertRaises(Exception):
            node = TextNode("This is text with **bold words inside.", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_split_nodes_multiple_nodes(self):
        node1 = TextNode("This is text with **bold words** inside.", TextType.TEXT)
        node2 = TextNode("This is text with _italic words_ inside.", TextType.TEXT)
        node3 = TextNode("This is code block.", TextType.CODE)
        new_nodes = split_nodes_delimiter([node1, node2, node3], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with ", TextType.TEXT),
                                     TextNode("bold words", TextType.BOLD),
                                     TextNode(" inside.", TextType.TEXT),
                                     TextNode("This is text with _italic words_ inside.", TextType.TEXT),
                                     TextNode("This is code block.", TextType.CODE)
                                    ]
                        )

if __name__ == "__main__":
    unittest.main()