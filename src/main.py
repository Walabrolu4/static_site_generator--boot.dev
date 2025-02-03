from enum import Enum
from textnode import *
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from node_transformer import text_node_to_html_node , split_nodes_by_delimiter , split_nodes_by_priority , extract_markdown_images , extract_markdown_links , split_nodes_link , split_nodes_image, text_to_textnodes
from block_transformer import markdown_to_blocks , get_block_type
from html_transformer import markdown_to_html_node

def basic_testing():
  
  text_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
  print(text_node.__repr__())
  print ("--------------------------------------")

  html_node = HTMLNode("b","This is words",None,{"url":"www.google.com" , "based":"bros"})
  print(html_node.__repr__())
  print ("--------------------------------------")
  leaf_node = LeafNode("google","a",{"url": "www.google.com"})
  print(leaf_node.to_html())
  print ("--------------------------------------")

  leaf_node2 = LeafNode("Is paying","b")
  leaf_node3 = LeafNode("reddit","a",{"url": "www.reddit.com"})
  parent_node = ParentNode("p",[leaf_node,leaf_node2,leaf_node3],None)
  print(parent_node.to_html())
  print ("--------------------------------------")

  converted_node = text_node_to_html_node(text_node)
  print(converted_node.to_html())
  print ("--------------------------------------")

  text_node2 = TextNode("This should be **split** and *stuff*",TextType.TEXT)
  split_nodes = split_nodes_by_priority([text_node2])
  print(split_nodes)

  print ("--------------------------------------")
  text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
  print(extract_markdown_images(text))
  # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

  print ("--------------------------------------")
  text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
  print(extract_markdown_links(text))
  # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

  print ("--------------------------------------")  
  link_node = TextNode("Start [link1](url1) middle [link2](url2) end", TextType.TEXT)
  print(split_nodes_link([link_node]))

  print ("--------------------------------------")  
  img_node = TextNode("Start ![img1](img_url1) middle ![img2](img_url2) end", TextType.TEXT)
  print(split_nodes_image([img_node]))

  print ("--------------------------------------")  
  text_to_convert = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
  converted_nodes = text_to_textnodes(text_to_convert)
  print(converted_nodes)

  print ("--------------------------------------")    
  markdown_text  ="# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
  #markdown_text = "Header\n\n   \n\nParagraph"  # Has a block with only spaces
  markdown_blocks = markdown_to_blocks(markdown_text)
  print(markdown_blocks)
  for texts in markdown_blocks:
    print(get_block_type(texts))

def main():
  #basic_testing()
  markdown = "# My Title\n\nThis is a paragraph with some *italic* and **bold** text.\n\n* First item\n* Second item\n\n> A wise quote"
  print(markdown_to_html_node(markdown))
  pass


main()