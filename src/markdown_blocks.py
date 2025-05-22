def markdown_to_blocks(markdown: str):
    """
    Split a full Markdown document into block-level strings.

    Rules:
      • Blocks are separated by one **or more** blank lines.
      • Leading/trailing whitespace inside each block is stripped.
      • Completely empty blocks are discarded.
    """
    # Normalize line endings (optional safety)
    normalized = markdown.replace("\r\n", "\n").strip()

    # Split on two or more consecutive newlines.
    raw_blocks = normalized.split("\n\n")

    # Clean up each block and discard empties
    blocks = [blk.strip() for blk in raw_blocks if blk.strip()]

    return blocks
