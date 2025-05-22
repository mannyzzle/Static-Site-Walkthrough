import re

def extract_markdown_images(text):
    """
    Extracts markdown image syntax ![alt](url) into a list of (alt, url) tuples.
    """
    return re.findall(r"!\[([^\]]+)\]\(([^)]+)\)", text)

def extract_markdown_links(text):
    """
    Extracts markdown link syntax [text](url) into a list of (text, url) tuples.
    Does NOT extract image links.
    """
    return re.findall(r"(?<!\!)\[([^\]]+)\]\(([^)]+)\)", text)
