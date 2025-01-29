import unittest
from textnode import *
from node_transformer import text_node_to_html_node, split_nodes_by_delimiter, split_nodes_by_priority, extract_markdown_links, extract_markdown_images , split_nodes_image, split_nodes_link , text_to_textnodes


class TestNodeTransformer(unittest.TestCase):
  def test_simple_conversion(self):
    text_node = TextNode("This is a text node", TextType.BOLD)
    converted_node = text_node_to_html_node(text_node)
    assert_str = "<b>This is a text node</b>"
    self.assertEqual(converted_node.to_html(),assert_str)
  
  def test_type_error(self):
    with self.assertRaises(Exception):
      text_node = TextNode("this is a text node",2)

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

  def test_simple_delimiter_transfrom(self):
    text_node = TextNode("This should be **split** and *stuff*",TextType.TEXT)
    split_nodes = split_nodes_by_delimiter([text_node],"**",TextType.BOLD)
    assert_list = [TextNode("This should be ", TextType.TEXT, None), TextNode("split", TextType.BOLD, None), TextNode(" and *stuff*", TextType.TEXT, None)]
    self.assertEqual(split_nodes,assert_list)

  def test_italics_delimiter_transform(self):
    text_node = TextNode("This should be **split** and *stuff*",TextType.TEXT)
    split_nodes = split_nodes_by_priority([text_node])
    assert_list = [TextNode("This should be ", TextType.TEXT , None), TextNode("split", TextType.BOLD, None), TextNode(" and ", TextType.TEXT, None), TextNode("stuff", TextType.ITALIC, None), TextNode("", TextType.TEXT, None)]
    self.assertEqual(split_nodes,assert_list)
  
  def test_split_nodes_raise_error(self):
    text_node = TextNode("This should be **split** and *stuff*",TextType.TEXT)
    with self.assertRaises(Exception):
      split_nodes = split_nodes_by_delimiter([text_node],"*",TextType.BOLD)
    
  def test_extract_image(self):
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    parsed_text = extract_markdown_images(text)
    assert_list = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
    self.assertEqual(parsed_text,assert_list)

  def test_extract_link(self):
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    parsed_text = extract_markdown_links(text)
    assert_list = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
    self.assertEqual(parsed_text,assert_list)
 
  def test_extract_image_exception(self):
    text = "This"
    parsed_text = extract_markdown_images(text)
    self.assertEqual(parsed_text,[])

  def test_extract_link_exception(self):
    text = "This"
    parsed_text = extract_markdown_links(text)
    self.assertEqual(parsed_text,[])

  def test_text_node_to_link_simple(self): 
    link_node = TextNode("Start [link1](url1) middle [link2](url2) end", TextType.TEXT)
    converted_nodes = split_nodes_link([link_node])
    self.assertEqual(converted_nodes[0].text,"Start ")
    self.assertEqual(converted_nodes[1].text,"link1")
    self.assertEqual(converted_nodes[3].url, "url2")
  
  def test_text_node_to_link_no_link(self):
    link_node = TextNode("Hello World",TextType.TEXT)
    converted_nodes = split_nodes_link([link_node])
    self.assertEqual(converted_nodes[0].text, "Hello World")

  def test_text_node_to_image_simple(self): 
    link_node = TextNode("Start ![link1](url1) middle ![link2](url2) end", TextType.TEXT)
    converted_nodes = split_nodes_image([link_node])
    self.assertEqual(converted_nodes[0].text,"Start ")
    self.assertEqual(converted_nodes[1].text,"link1")
    self.assertEqual(converted_nodes[3].url, "url2")
  
  def test_text_node_to_image_no_link(self):
    link_node = TextNode("Hello World",TextType.TEXT)
    converted_nodes = split_nodes_image([link_node])
    self.assertEqual(converted_nodes[0].text, "Hello World")

  def test_text_to_textnode(self):
    text_to_convert = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    converted_nodes = text_to_textnodes(text_to_convert)
    self.assertEqual(converted_nodes[0].text,"This is ")
    self.assertEqual(converted_nodes[1].text_type,TextType.BOLD)
    self.assertEqual(converted_nodes[-1].url,"https://boot.dev")
