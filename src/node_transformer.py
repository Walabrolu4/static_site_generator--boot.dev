from textnode import *
from leafnode import LeafNode
def text_node_to_html_node(text_node):
  match (text_node.text_type):
    case TextType.TEXT:
      return LeafNode(text_node.text)
    case TextType.BOLD:
      return LeafNode(text_node.text,"b")
    case TextType.ITALIC:
      return LeafNode(text_node.text,"i")
    case TextType.CODE:
      return LeafNode(text_node.text,"code")
    case TextType.LINK:
      return LeafNode(text_node.text,"a",{"href": text_node.url})
    case TextType.IMAGE:
      return LeafNode("","img",{"src" : text_node.url , "alt" : text_node.text})
    case _:
      raise Exception("Not a valid text type")


def split_nodes_by_priority(old_nodes):
    # Define delimiter processing order
    priority = [
        ("**", TextType.BOLD),
        ("*", TextType.ITALIC),
        ("`", TextType.CODE),
    ]

    new_nodes = old_nodes

    # Process each delimiter in order of priority
    for delimiter, text_type in priority:
        new_nodes = split_nodes_by_delimiter(new_nodes, delimiter, text_type)

    return new_nodes

def split_nodes_by_delimiter(old_nodes,delimiter,text_type):

  if not old_nodes:
    raise Exception("node list cannot be empty!") 
  
  valid_delimiters = {
    "**": TextType.BOLD,
    "*": TextType.ITALIC,
    "`": TextType.CODE,   
  }
  
  if delimiter not in valid_delimiters:
    raise Exception(f"Invalid delimiter '{delimiter}' provided.")
  if valid_delimiters[delimiter] != text_type:
    raise Exception(f"Mismatch between delimiter '{delimiter}' and text type '{text_type}'. Expected '{valid_delimiters[delimiter]}'.")


  new_nodes = list()
  
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      new_nodes.append(node)

    else:
      delimited_list = node.text.split(delimiter)
      raise_delimited_error(delimited_list,delimiter)
      new_nodes.extend(append_delimited_list(delimited_list, text_type))
  return new_nodes


def raise_delimited_error(delimited_list,delimiter):
  if len(delimited_list) % 2 != 1:
    raise Exception (f"Found opening {delimiter} but not closing")
  
def append_delimited_list(delimited_list,text_type):
  new_nodes = list()
  count = 0
  for text in delimited_list:
    if count % 2 == 1:
      new_nodes.append(TextNode(text,text_type))
    else:
      new_nodes.append(TextNode(text,TextType.TEXT))
    count += 1
  return new_nodes


'''
TEXT  (nothing)
BOLD  **
ITALIC  *
CODE  ```
LINK  [link]
IMAGE  ![]
'''

