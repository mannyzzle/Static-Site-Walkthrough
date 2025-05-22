from parentnode import ParentNode
from leafnode import LeafNode
from markdown_blocks import markdown_to_blocks
from block_types import BlockType, block_to_block_type
from text_to_textnodes import text_to_textnodes
from converters import text_node_to_html_node

def markdown_to_html_node(markdown: str) -> ParentNode:
    """
    Convert a full Markdown doc (string) into a single <div> HTMLNode tree.
    """
    blocks   = markdown_to_blocks(markdown)
    children = [ _block_to_html_node(b) for b in blocks ]
    return ParentNode("div", children)





def _block_to_html_node(block: str) -> ParentNode | LeafNode:
    btype = block_to_block_type(block)

    if btype == BlockType.HEADING:
        return _heading_to_html(block)

    if btype == BlockType.CODE:
        return _code_to_html(block)

    if btype == BlockType.QUOTE:
        return _quote_to_html(block)

    if btype == BlockType.UNORDERED_LIST:
        return _ul_to_html(block)

    if btype == BlockType.ORDERED_LIST:
        return _ol_to_html(block)

    # default → paragraph
    return _paragraph_to_html(block)



def _text_to_children(text: str):
    """Shared inline-parser → returns a list[HTMLNode]"""
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(tn) for tn in text_nodes]


def _heading_to_html(block: str) -> ParentNode:
    level  = len(block.split(" ")[0])          # number of # chars
    text   = block[level+1:]                   # strip '# ' prefix
    return ParentNode(f"h{level}", _text_to_children(text))


def _paragraph_to_html(block: str) -> ParentNode:
    # Collapse internal newlines → single spaces
    clean = " ".join(block.splitlines())
    return ParentNode("p", _text_to_children(clean))

def _code_to_html(block: str) -> ParentNode:
    code_body = "\n".join(block.splitlines()[1:-1]) + "\n"
    code_leaf = LeafNode(None, code_body)          # raw text
    code_node = ParentNode("code", [code_leaf])
    return ParentNode("pre", [code_node])


def _quote_to_html(block: str) -> ParentNode:
    inner = "\n".join(line[2:] for line in block.splitlines())
    return ParentNode("blockquote", _text_to_children(inner))


def _ul_to_html(block: str) -> ParentNode:
    li_nodes = [
        ParentNode("li", _text_to_children(line[2:]))
        for line in block.splitlines()
    ]
    return ParentNode("ul", li_nodes)


def _ol_to_html(block: str) -> ParentNode:
    li_nodes = [
        ParentNode("li", _text_to_children(line.split(". ", 1)[1]))
        for line in block.splitlines()
    ]
    return ParentNode("ol", li_nodes)
