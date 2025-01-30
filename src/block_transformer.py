from enum import Enum
import re
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

def filter_whitespace(item_to_filter):
  if item_to_filter == "":
    return False
  else:
    return True
  