from enum import Enum
class BlockType(Enum):
  PARAGRAPH = "paragrah",
  HEADING = "heading",
  CODE = "code",
  QUOTE = "quote",
  UO_LIST = "uo_list"
  O_LIST = "o_list"

def markdown_to_blocks(markdown):
  markdown_list = markdown.split("\n\n")
  markdown_list = list(map(str.strip,markdown_list))
  markdown_list = list(filter(filter_whitespace,markdown_list))
  return(markdown_list)

'''  markdown_list = markdown.split("\n\n")
  markdown_list_copy = markdown_list.copy()
  for i in range(0,len(markdown_list)):
    markdown_list_copy[i] = markdown_list[i].strip()
    if markdown_list[i] == "\n" or markdown_list[i] == "":
      markdown_list_copy.pop(i)
  markdown_list = markdown_list_copy.copy()
  '''
def get_block_type(markdown):
  if markdown[0] == "#":
    return BlockType.HEADING
  if len(markdown.split("```")) == 2:
    return BlockType.CODE
  if markdown[0] == ">":
    return BlockType.QUOTE
  if markdown[0] == "*" or markdown[0] == "-":
    return BlockType.UO_LIST
  if markdown[:2] == "1. ":
    return BlockType.O_LIST
  

def filter_whitespace(item_to_filter):
  if item_to_filter == "":
    return False
  else:
    return True
  