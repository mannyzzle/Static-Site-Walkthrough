from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag.")
        if children is None:
            raise ValueError("ParentNode must have children.")
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        inner_html = "".join(child.to_html() for child in self.children)
        props_str = ""
        if self.props:
            props_str = " " + " ".join(f'{k}="{v}"' for k, v in self.props.items())
        return f"<{self.tag}{props_str}>{inner_html}</{self.tag}>"

