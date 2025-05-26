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
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, text_node.url)
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", text_node.url)
    raise Exception("Incorrect or no TextType")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old in old_nodes:
        if old.text_type != TextType.TEXT:
            new_nodes.append(old)
        else:
            if delimiter in old.text:
                if (old.text.count(delimiter)) % 2 != 0:
                    raise Exception("Closing delimiter not found")
                else:
                    split_text = old.text.split(sep=delimiter)
                    for s in split_text:
                        if split_text.index(s) % 2 != 0:
                            new_nodes.append(TextNode(s, text_type))
                        else:
                            new_nodes.append(TextNode(s, TextType.TEXT))
            else:
                new_nodes.append(old)
            
    return new_nodes