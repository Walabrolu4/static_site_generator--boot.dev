import unittest
from textnode import *
from node_transformer import text_node_to_html_node


class TestNodeTransformer(unittest.TestCase):
  def test_simple_conversion(self):
    text_node = TextNode("This is a text node", TextType.BOLD)
    converted_node = text_node_to_html_node(text_node)
    assert_str = "<b>This is a text node</b>"
    self.assertEqual(converted_node.to_html(),assert_str)
  
  def test_type_error(self):
    text_node = TextNode("this is a text node",2)
    self.assertRaises(Exception)

  def test_url_conversion(self):
    text_node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
    converted_node = text_node_to_html_node(text_node)
    assert_str = "<a href=\"https://www.boot.dev\">This is a text node</a>"
    self.assertEqual(converted_node.to_html(),assert_str)

  def test_img_conversion(self):
    text_node = TextNode("This is a image", TextType.IMAGE, "imgs/dandy.png")
    converted_node = text_node_to_html_node(text_node)
    assert_str = "<img src=\"imgs/dandy.png\"alt=\"This is a image\"></img>"
    self.assertEqual(converted_node.to_html(),assert_str)