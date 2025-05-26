from textnode import TextNode, TextType
import re


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

def extract_markdown_images(text):
    image_list = []
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    image_list.extend(matches)
    return image_list

def extract_markdown_links(text):
    link_list = []
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    link_list.extend(matches)
    return link_list