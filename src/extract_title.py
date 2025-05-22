import re

def extract_title(markdown: str) -> str:
    """
    Return the first H1 text (line starting with exactly one '# ').
    Raise ValueError if none found.
    """
    for line in markdown.splitlines():
        if re.match(r"^#[^#]", line):
            return line.lstrip("#").strip()
    raise ValueError("Markdown has no H1 title")


