from blocktype import block_to_block_type, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdowninterpreter import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes, markdown_to_blocks
from textnode import TextType, TextNode, text_node_to_html_node

def markdown_to_html_node(markdown):
    div = ParentNode("div", [])
    split_markdown = markdown_to_blocks(markdown)
    
    for b in split_markdown:
        block_type = block_to_block_type(b)
        node = None
        
        if block_type == BlockType.PARAGRAPH:
            node = ParentNode("p", text_to_children(b), None)
            div.children.append(node)
        elif block_type == BlockType.HEADING:
            pass

        elif block_type == BlockType.CODE:
            code_node = text_node_to_html_node(TextNode(b, TextType.CODE))
            code_node.tag = "code"
            node = ParentNode("pre", code_node)
            div.children.append(node)

        elif block_type == BlockType.QUOTE:
            pass

        elif block_type == BlockType.UNORDERED_LIST:
            pass

        elif block_type == BlockType.ORDERED_LIST:
            pass

        
    
    return div


def text_to_children(text):
    children_list = []
    text_node = TextNode(text, TextType.TEXT)
    node_list = [text_node]
    node_list = split_nodes_delimiter(node_list, "**", TextType.BOLD)
    node_list = split_nodes_delimiter(node_list, "_", TextType.ITALIC)
    node_list = (split_nodes_delimiter(node_list, "`", TextType.CODE))
    node_list = (split_nodes_image(node_list))
    node_list = (split_nodes_link(node_list))
    
    for n in node_list:
        children_list.append(text_node_to_html_node(n))

    return children_list