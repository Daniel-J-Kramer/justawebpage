import unittest

from blocktype import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):

    def test_block_to_block_type(self):
        type = BlockType.PARAGRAPH
        block = "This is a block of text"
        self.assertEqual(type, block_to_block_type(block))
        pass

    def test_block_to_block_type_heading(self):
        type = BlockType.HEADING
        block = "###### This is a heading block"
        self.assertEqual(type, block_to_block_type(block))

    def test_block_to_block_type_heading_too_long(self):
        type = BlockType.PARAGRAPH
        block = "######## This is a paragraph block"
        self.assertEqual(type, block_to_block_type(block))

    def test_block_to_block_type_code(self):
        type = BlockType.CODE
        block = "```This is a code block```"
        self.assertEqual(type, block_to_block_type(block))

    def test_block_to_block_type_quote(self):
        type = BlockType.QUOTE
        block = """
>This is a quote block
>This has more lines too
"""
        self.assertEqual(type, block_to_block_type(block))

    def test_block_to_block_type_unordered_list(self):
        type = BlockType.UNORDERED_LIST
        block = """
- This is an
- unordered list
"""
        self.assertEqual(type, block_to_block_type(block))

    def test_block_to_block_type_ordered_list(self):
        type = BlockType.ORDERED_LIST
        block = """
1. This is an
2. Ordered list
"""
        self.assertEqual(type, block_to_block_type(block))

if __name__ == "__main__":
    unittest.main()