import unittest
from block_transformer import markdown_to_blocks
class TestBlockTransformer(unittest.TestCase):
  def test_blocktransformer_simple(self):
    markdown_text  ="# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
    converted_nodes = markdown_to_blocks(markdown_text)
    self.assertEqual(converted_nodes[0],"# This is a heading")

  def test_blocktransformer_extralinebreak(self):
    markdown_text = "Header\n\n   \n\nParagraph"
    converted_nodes = markdown_to_blocks(markdown_text)
    self.assertEqual(converted_nodes,["Header","Paragraph"])