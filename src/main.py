from enum import Enum
from textnode import *
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
def main():
  test_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
  html_node = HTMLNode("b","This is words",None,{"url":"www.google.com" , "based":"bros"})
  leaf_node = LeafNode("google","a",{"url": "www.google.com"})
  leaf_node2 = LeafNode("Is paying","b")
  leaf_node3 = LeafNode("reddit","a",{"url": "www.reddit.com"})
  parent_node = ParentNode("p",[leaf_node,leaf_node2,leaf_node3],None)
  print(test_node.__repr__())
  print(html_node.__repr__())
  print(leaf_node.to_html())
  print(parent_node.to_html())

main()