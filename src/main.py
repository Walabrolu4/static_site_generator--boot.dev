from enum import Enum
from textnode import *
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from node_transformer import text_node_to_html_node , split_nodes_by_delimiter , split_nodes_by_priority , extract_markdown_images , extract_markdown_links
def main():

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

main()