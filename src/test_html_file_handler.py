import unittest
from html_file_handler import *

class TestFileHandler(unittest.TestCase):
  def test_extract_heading(self):
    markdown = "# My Title\n\nThis is a paragraph with some *italic* and **bold** text.\n\n* First item\n* Second item\n\n> A wise quote"
    title = extract_title(markdown)
    self.assertEqual(title,"My Title")

  def test_extract_heading_err(self):
    markdown = "My Title\n\nThis is a paragraph with some *italic* and **bold** text.\n\n* First item\n* Second item\n\n> A wise quote"
    with self.assertRaises(Exception):
      title = extract_title(markdown)

  def generate_page(from_path,template_path,dest_path):
    print(f"generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path,'r') as f:
      markdown_text = f.read()
    print(markdown_text)
    pass