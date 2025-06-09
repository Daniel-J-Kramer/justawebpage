from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "Paragraph Block"
    HEADING = "# Heading Block"
    CODE = "```Code Block```"
    QUOTE = ">Quote Block"
    UNORDERED_LIST = "- Unordered_List Block"
    ORDERED_LIST = "1. Ordered_List Block"

def block_to_block_type(block):
    Type = BlockType.PARAGRAPH

    for ch in range(0, len(block)):
        
        if block[ch] == "#" and  block[ch + 1] == " ":
            if ch < 6:
                return BlockType.HEADING
            else:
                Type = BlockType.PARAGRAPH
    
    if block[0:3] == "```":
        if block[:-4:-1] == block[0:3]:
            return BlockType.CODE

    if "\n" in block:
        strings = block.split(sep="\n")
        count = 1
        for string in strings:
            if string.startswith(">"):
                Type = BlockType.QUOTE
            elif string.startswith("- "):
                Type = BlockType.UNORDERED_LIST
            elif string[0:3] == f"{count}. ":
                count += 1
                Type = BlockType.ORDERED_LIST
                
    return Type