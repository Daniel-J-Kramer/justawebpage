from blocktype import block_to_block_type, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdowninterpreter import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes, markdown_to_blocks
from textnode import TextType, TextNode, text_node_to_html_node

def markdown_to_html_node(markdown):
    new_parent_node = None

    split_markdown = markdown_to_blocks(markdown)
    
    for b in split_markdown:
        block_type = block_to_block_type(b)
        if block_type == BlockType.PARAGRAPH:
            pass
        elif block_type == BlockType.HEADING:
            pass
        elif block_type == BlockType.CODE:
            pass
        elif block_type == BlockType.QUOTE:
            pass
        elif block_type == BlockType.UNORDERED_LIST:
            pass
        elif block_type == BlockType.ORDERED_LIST:
            pass

    return new_parent_node