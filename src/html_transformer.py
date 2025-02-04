from block_transformer import markdown_to_blocks, get_block_type, block_to_HTML_node , BlockType
from node_transformer import text_node_to_html_node , split_nodes_by_delimiter , split_nodes_by_priority , extract_markdown_images , extract_markdown_links , split_nodes_link , split_nodes_image, text_to_textnodes
from leafnode import LeafNode
from parentnode import ParentNode


def markdown_to_html_node(markdown):
  markdown_blocks = markdown_to_blocks(markdown)
  html_nodes = list()
  for block in markdown_blocks:
    block_type = get_block_type(block)
    if block_type == BlockType.UO_LIST:
        #Remove the list markers before processing inline formatting
        cleaned_block = "\n".join(line[1:].strip() for line in block.splitlines())
        block = cleaned_block
    block = text_to_textnodes(block)
    html_content = ""
    for node in block:
      html_content += text_node_to_html_node(node).to_html()
    #print(html_content)
    html_nodes.append(block_to_HTML_node(html_content,block_type))
  return ParentNode("div",html_nodes)

'''
def markdown_to_html_node(markdown):
  markdown_blocks = markdown_to_blocks(markdown)
  html_nodes = list()
  for block in markdown_blocks:
    block_type = get_block_type(block)
    print(block)
    block = text_to_textnodes(block)
    html_content = ""
    for node in block:
      html_content += text_node_to_html_node(node).to_html()
    print(html_content)
    html_nodes.append(block_to_HTML_node(html_content,block_type))
  return ParentNode("div",html_nodes)
'''

'''Steps
1. Split markdown into blocks
2. Loop over each block
    2.1 Determine the type of block
    2.2 Based on the block create a new HTMLNode with the proper data
    2.3 Assign the proper child HTMLNode to the block node
3. Make all the block nodes children under a single Parent HTMLNode which is a DIV

  PARAGRAPH = "paragraph",
  HEADING = "heading",
  CODE = "code",
  QUOTE = "quote",
  UO_LIST = "uo_list"
  O_LIST = "o_list"

'''
