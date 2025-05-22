from enum import Enum, auto
import re

class BlockType(Enum):
    PARAGRAPH       = auto()
    HEADING         = auto()
    CODE            = auto()
    QUOTE           = auto()
    UNORDERED_LIST  = auto()
    ORDERED_LIST    = auto()

_HEADING_RE       = re.compile(r"^#{1,6} ")
_CODE_FENCE       = "```"
_QUOTE_RE         = re.compile(r"^> ")
_UNORDERED_RE     = re.compile(r"^- ")
_ORDERED_RE_FIRST = re.compile(r"^1\. ")
_ORDERED_RE       = re.compile(r"^(\d+)\. ")

def block_to_block_type(block: str) -> BlockType:
    """
    Determine the BlockType of a markdown block.
    Assumes `block` is already stripped of leading/trailing whitespace.
    """

    # ----- CODE BLOCK ------------
    if block.startswith(_CODE_FENCE) and block.rstrip().endswith(_CODE_FENCE):
        return BlockType.CODE

    lines = block.splitlines()

    # ----- HEADING ---------------
    if _HEADING_RE.match(lines[0]):
        return BlockType.HEADING

    # ----- QUOTE -----------------
    if all(line.startswith(">") or line.strip() == "" for line in lines):
        return BlockType.QUOTE

    # ----- UNORDERED LIST --------
    if all(_UNORDERED_RE.match(line) for line in lines):
        return BlockType.UNORDERED_LIST

    # ----- ORDERED LIST ----------
    if _ORDERED_RE_FIRST.match(lines[0]):
        expected = 1
        for line in lines:
            m = _ORDERED_RE.match(line)
            if not m or int(m.group(1)) != expected:
                break
            expected += 1
        else:  # only executes if loop didn’t break
            return BlockType.ORDERED_LIST

    # ----- PARAGRAPH (default) ---
    return BlockType.PARAGRAPH
