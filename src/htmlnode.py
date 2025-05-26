

class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props_string = ""
        if self.props != None:
            for d in self.props:
                prop = self.props[d]
                props_string += f'{d}="{prop}" '
            props_string = props_string.strip()
            props_string = " " + props_string
        return props_string

    def __eq__(node, node2):
        if node.tag == node2.tag:
            if node.value == node2.value:
                if node.children == node2.children:
                    if node.props == node2.props:
                        return True
        return False

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
         super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("value required")
        elif self.tag == None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag required")
        elif self.children == None:
            raise ValueError("child(ren) requried")
        else:
            child_string = ""
            for c in self.children:
                child_string += c.to_html()
            return f"<{self.tag}{self.props_to_html()}>{child_string}</{self.tag}>"