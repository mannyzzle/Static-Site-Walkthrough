from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_media import split_nodes_image, split_nodes_link

def text_to_textnodes(text: str):
    """
    Convert raw markdown-style text into a list of TextNode objects.

    Order of operations (important):
      1. Inline code  ( `code` )
      2. Bold         ( **bold** )
      3. Italic       ( _italic_ )
      4. Images       ( ![alt](url) )
      5. Links        ( [text](url) )

    Each splitter only touches TextType.TEXT nodes, so chaining is safe.
    """
    nodes = [TextNode(text, TextType.TEXT)]

    # 1. code blocks
    nodes = split_nodes_delimiter(nodes, "`",  TextType.CODE)
    # 2. bold
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    # 3. italic
    nodes = split_nodes_delimiter(nodes, "_",  TextType.ITALIC)
    # 4. images
    nodes = split_nodes_image(nodes)
    # 5. links (after images so "![...](...)" isn't treated as a link)
    nodes = split_nodes_link(nodes)

    return nodes
