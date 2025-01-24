import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_eq(self):
    leaf_node = LeafNode("a","google",{"url": "www.google.com"})
    formatted_html = "<a url=\"www.google.com\">google<\\a>"
    self.assertEqual(leaf_node.to_html(),formatted_html)