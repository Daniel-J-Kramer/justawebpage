import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_eq(self):
        node = HTMLNode("p", "Just some text", None, {'href: "https://www.google.com"'})
        node2 = HTMLNode("p", "Just some text", None, {'href: "https://www.google.com"'})
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = HTMLNode("a", "Just some text", None, {'href: "https://www.google.com"'})
        node2 = HTMLNode("p", "Just some text", None, {'href: "https://www.google.com"'})
        self.assertNotEqual(node, node2)

    def test_props(self):
        node = HTMLNode("a", "Just some text", None, {"href": "https://www.google.com"})
        test = node.props_to_html()
        expected = ' href="https://www.google.com"'
        self.assertEqual(test, expected)

    def test_2props(self):
        node = HTMLNode("a", "Just some text", None, {"href": "https://www.google.com", "target": "_blank"})
        test = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(test, expected)

if __name__ == "__main__":
    unittest.main()