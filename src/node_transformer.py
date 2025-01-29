from textnode import *
from leafnode import LeafNode
import re
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

def text_to_textnodes(text):
  text_list = list()
  text_node = TextNode(text,TextType.TEXT)
  text_list.append(text_node)

  text_list = split_nodes_link(text_list)
  text_list = split_nodes_image(text_list)

  text_list = split_nodes_by_priority(text_list)
  return text_list

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

def split_nodes_link(old_nodes):
  if not old_nodes:
    raise Exception("node list cannot be empty!")

  new_nodes = list()
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      new_nodes.append(node)

    else:
      remaining_text = node.text
      extracted_links = extract_markdown_links(node.text)
      if extracted_links:
        for link_text, link_url in extracted_links:
          section = remaining_text.split(f"[{link_text}]({link_url})",1)
          if section[0] != "":
            new_nodes.append(TextNode(section[0],TextType.TEXT))
          new_nodes.append(TextNode(f"{link_text}",TextType.LINK,f"{link_url}"))
          remaining_text = section[1]
        if remaining_text != "":
          new_nodes.append(TextNode(remaining_text,TextType.TEXT))
      else:
        new_nodes.append(node)
  return new_nodes
    

def split_nodes_image(old_nodes):
  if not old_nodes:
    raise Exception("node list cannot be empty!")
  
  new_nodes = list()
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      new_nodes.append(node)

    else:
      remaining_text = node.text
      extracted_images = extract_markdown_images(node.text)
      if extracted_images:
        for img_alt , img_link in extracted_images:
          section = remaining_text.split(f"![{img_alt}]({img_link})",1)
          if section[0] != "":
            new_nodes.append(TextNode(section[0],TextType.TEXT))
          new_nodes.append(TextNode(f"{img_alt}",TextType.IMAGE,f"{img_link}"))
          remaining_text = section[1]
        if remaining_text != "":
          new_nodes.append(TextNode(remaining_text,TextType.TEXT))
      else:
        new_nodes.append(node)
  return new_nodes

def extract_markdown_images(text):
  parsed_text = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)" , text)
  return parsed_text

def extract_markdown_links(text):
  parsed_text = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
  return parsed_text

'''
TEXT  (nothing)
BOLD  **
ITALIC  *
CODE  ```
LINK  [link]
IMAGE  ![]
'''

