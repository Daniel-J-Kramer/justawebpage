import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )      

    def test_parent_with_multiple_children(self):
        child_node1 = LeafNode("b", "child1")
        child_node2 = LeafNode(None, "child2")
        child_node3 = LeafNode("i", "child3")
        parent_node = ParentNode("p", [child_node1, child_node2, child_node3])
        self.assertEqual(parent_node.to_html(), "<p><b>child1</b>child2<i>child3</i></p>")

    def test_parent_with_multiple_parent_child(self):
        grandchild_node1 = LeafNode("b", "grandchild")
        child_node1 = ParentNode("span", [grandchild_node1])
        grandchild_node2 = LeafNode("i", "grandchild2")
        child_node2 = ParentNode("span", [grandchild_node2])
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span><span><i>grandchild2</i></span></div>",
        )

    def test_parent_with_prop_and_child(self):
        child_node = LeafNode("b", "Some Text")
        parent_node = ParentNode("p", [child_node], {"href": "https://www.google.com"})
        self.assertEqual(
            parent_node.to_html(), 
            "<p href=\"https://www.google.com\"><b>Some Text</b></p>",
        )

    def test_parent_with_child_prop(self):
        child_node = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        parent_node = ParentNode("p", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<p><a href=\"https://www.google.com\">Click Me!</a></p>"
        )

    def test_tag_error(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode(None, [LeafNode("b", "Text")])
            parent_node.to_html()
        

    def test_children_error(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode("p", None)
            parent_node.to_html()
        pass