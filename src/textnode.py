from enum import Enum

from htmlnode import LeafNode, ParentNode, HTMLNode

class TextType(Enum):
    TEXT = "Normal text"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "'Code text'"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"

class TextNode():

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(node, node2):
        if node.text == node2.text:
            if node.text_type == node2.text_type:
                if node.url == node2.url:
                    return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    text = text_node.text
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text, text_node.url)
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", text_node.url)
    raise Exception("Incorrect or no TextType")