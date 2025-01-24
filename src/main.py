from enum import Enum
from textnode import *
from htmlnode import HTMLNode
from leafnode import LeafNode
def main():
  test_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
  html_node = HTMLNode("b","This is words",None,{"url":"www.google.com" , "based":"bros"})
  leaf_node = LeafNode("a","google",{"url": "www.google.com"})
  print(test_node.__repr__())
  print(html_node.__repr__())
  print(leaf_node.to_html())

main()