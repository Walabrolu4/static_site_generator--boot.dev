from enum import Enum
import re
from leafnode import LeafNode
from parentnode import ParentNode
class BlockType(Enum):
  PARAGRAPH = "paragraph",
  HEADING = "heading",
  CODE = "code",
  QUOTE = "quote",
  UO_LIST = "uo_list"
  O_LIST = "o_list"



def get_block_type(markdown):
  if markdown[0] == "#":
    if re.findall(r"\#{1,6} .+",markdown):
      return BlockType.HEADING
    
  if markdown[:3] == "```" and markdown[-3:] == "```":
    return BlockType.CODE

  if markdown[:2] == "> ":
    split_lines = markdown.split("\n")
    for lines in split_lines:
      lines = lines.strip()
      if lines[:2] != "> ":
        return BlockType.PARAGRAPH
    return BlockType.QUOTE
        
  if markdown[:2] == "* " or markdown[:2] == "- ":
    split_lines = markdown.split("\n")
    for lines in split_lines:
      lines = lines.strip()
      if lines[:2] != "* " :
        if lines[:2] != "- ":
          return BlockType.PARAGRAPH
    return BlockType.UO_LIST
  
  if markdown[:3] == "1. ":
    split_lines = markdown.split("\n")
    count = 1
    for lines in split_lines:
      lines = lines.strip()
      if lines[:3] != f"{count}. ":
        return BlockType.PARAGRAPH
      count += 1
    return BlockType.O_LIST
  
  return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
  markdown_list = markdown.split("\n\n")
  markdown_list = list(map(str.strip,markdown_list))
  markdown_list = list(filter(filter_whitespace,markdown_list))
  return(markdown_list)

def block_to_HTML_node(text,block_type):
  match block_type:
    case BlockType.PARAGRAPH:
      return LeafNode(text,"p")
    
    case BlockType.HEADING:
      level = 0
      for char in text:
        if char == '#':
          level += 1
        else:
          break
      text = text[level:].strip()
      return LeafNode(text, f"h{level}")
    
    case BlockType.CODE:
      text_list = text.splitlines()
      del text_list[0]
      del text_list[-1]
      text = "\n".join(text_list)
      leaf = LeafNode(text,"code")
      return ParentNode("pre",[leaf])
    
    case BlockType.QUOTE:
      text = text[1:]
      text = text.strip()
      return LeafNode(text,"blockquote")
    
    case BlockType.UO_LIST:
      uo_list = list()
      for line in text.splitlines():
        #line = line[1:]
        line = line.strip()
        uo_list.append(LeafNode(line,"li"))
      return (ParentNode("ul",uo_list))

    case BlockType.O_LIST:
      o_list = list()
      for line in text.splitlines():
        line = line.split(".",1)
        line = line[1]
        line = line.strip()
        o_list.append(LeafNode(line,"li"))
      return ParentNode("ol",o_list)
    
    case _:
      raise Exception (f"{block_type} is not a valid block type")

def filter_whitespace(item_to_filter):
  if item_to_filter == "":
    return False
  else:
    return True
  