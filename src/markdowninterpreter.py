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
                        elif s != "":
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

def split_nodes_image(old_nodes):
    new_nodes = []
    for old in old_nodes:
        if old.text_type != TextType.TEXT:
            new_nodes.append(old)
        else:
            parse_string = old.text
            link_list = extract_markdown_images(old.text)
            text_only = []
            for t in link_list:
                image_alt = t[0]
                image_link = t[1]
                split_text = parse_string.split(f"![{image_alt}]({image_link})", 1)
                text_only.append(split_text[0])
                parse_string = parse_string.replace(split_text[0] + f"![{image_alt}]({image_link})", "")
            text_only.append(parse_string)
            text_nodes = []
            link_nodes = []
            for t in text_only:
                text_nodes.append(TextNode(t, TextType.TEXT))
            for l in link_list:
                link_nodes.append(TextNode(l[0], TextType.IMAGE, l[1]))
            if len(text_nodes) > len(link_nodes):
                for t in text_nodes:
                    index = text_nodes.index(t)
                    new_nodes.append(text_nodes[index])
                    if len(link_nodes) > index:
                        new_nodes.append(link_nodes[index])
            elif len(text_nodes) < len(link_nodes):
                for l in link_nodes:
                    index = link_nodes.index(l)
                    new_nodes.append(link_nodes[index])
                    if len(text_nodes) > index:
                        new_nodes.append(text_nodes[index])
            else:
                index = 0
                while index < len(text_nodes):
                    new_nodes.append(text_nodes[index])
                    new_nodes.append(link_nodes[index])
                    index += 1
    for n in new_nodes:
        if n.text == "":
            index = new_nodes.index(n)
            del new_nodes[index]

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old in old_nodes:
        if old.text_type != TextType.TEXT:
            new_nodes.append(old)
        else:
            parse_string = old.text
            link_list = extract_markdown_links(old.text)
            text_only = []
            for t in link_list:
                link_alt = t[0]
                link_link = t[1]
                split_text = parse_string.split(f"[{link_alt}]({link_link})", 1)
                text_only.append(split_text[0])
                parse_string = parse_string.replace(split_text[0] + f"[{link_alt}]({link_link})", "")
            text_only.append(parse_string)
            text_nodes = []
            link_nodes = []
            for t in text_only:
                text_nodes.append(TextNode(t, TextType.TEXT))
            for l in link_list:
                link_nodes.append(TextNode(l[0], TextType.LINK, l[1]))
            if len(text_nodes) > len(link_nodes):
                for t in text_nodes:
                    index = text_nodes.index(t)
                    new_nodes.append(text_nodes[index])
                    if len(link_nodes) > index:
                        new_nodes.append(link_nodes[index])
            elif len(text_nodes) < len(link_nodes):
                for l in link_nodes:
                    index = link_nodes.index(l)
                    new_nodes.append(link_nodes[index])
                    if len(text_nodes) > index:
                        new_nodes.append(text_nodes[index])
            else:
                index = 0
                while index < len(text_nodes):
                    new_nodes.append(text_nodes[index])
                    new_nodes.append(link_nodes[index])
                    index += 1
    for n in new_nodes:
        if n.text == "":
            index = new_nodes.index(n)
            del new_nodes[index]
            
        
    return new_nodes

def text_to_textnodes(text):
    new_nodes = []
    node = TextNode(text, TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes

def markdown_to_blocks(markdown):
    block_list = []
    split_list = markdown.split(sep=f"\n\n")
    for s in split_list:
        new_string = s.strip()
        if s.strip() != "":
            block_list.append(s.strip())
    
    return block_list