import re
from textnode import TextNode, TextType

# Regex patterns (used in markdown)
_IMG_RE  = re.compile(r"!\[([^\]]+)\]\(([^)]+)\)")
_LINK_RE = re.compile(r"(?<!\!)\[([^\]]+)\]\(([^)]+)\)")

def _split_nodes_generic(old_nodes, pattern, rich_type):
    """
    Helper: split any TEXT nodes inside `old_nodes` that match `pattern`.
    `rich_type` is TextType.IMAGE or TextType.LINK.
    """
    new_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = list(pattern.finditer(text))
        if not matches:
            new_nodes.append(node)
            continue

        last = 0
        for m in matches:
            start, end = m.span()

            # Plain text before match
            if start > last:
                new_nodes.append(TextNode(text[last:start], TextType.TEXT))

            label, url = m.groups()
            new_nodes.append(TextNode(label,
                                      rich_type,
                                      url))

            last = end

        # Trailing plain text
        if last < len(text):
            new_nodes.append(TextNode(text[last:], TextType.TEXT))

    return new_nodes


def split_nodes_image(old_nodes):
    """Split TEXT nodes by markdown image syntax."""
    return _split_nodes_generic(old_nodes, _IMG_RE, TextType.IMAGE)


def split_nodes_link(old_nodes):
    """Split TEXT nodes by markdown link syntax (excluding images)."""
    return _split_nodes_generic(old_nodes, _LINK_RE, TextType.LINK)
