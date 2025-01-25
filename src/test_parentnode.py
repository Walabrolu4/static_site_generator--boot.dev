import unittest
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
  def test_single_child(self):
    leaf_node = LeafNode("example text")
    parent_node = ParentNode("p",[leaf_node])
    assert_str = "<p>example text</p>"
    self.assertEqual(parent_node.to_html(),assert_str)

  def test_multi_child(self):
    leaf_node = LeafNode("google","a",{"url": "www.google.com"})
    leaf_node2 = LeafNode("Is paying","b")
    leaf_node3 = LeafNode("reddit","a",{"url": "www.reddit.com"})
    parent_node = ParentNode("p",[leaf_node,leaf_node2,leaf_node3],None)
    assert_str = "<p><a url=\"www.google.com\">google</a><b>Is paying</b><a url=\"www.reddit.com\">reddit</a></p>"
    self.assertEqual(parent_node.to_html(),assert_str)

  def test_multi_parent(self):
    leaf_node = LeafNode("google","a",{"url": "www.google.com"})
    leaf_node2 = LeafNode("Is paying","b")
    leaf_node3 = LeafNode("reddit","a",{"url": "www.reddit.com"})
    parent_node = ParentNode("p",[leaf_node,leaf_node2,leaf_node3],None)

    leaf_node4 = LeafNode("Also dont forget")
    leaf_node5 = LeafNode("facebook.com","a",)
    parent_node2 = ParentNode("p",[leaf_node4,leaf_node5,parent_node])
    assert_str = "<p>Also dont forget<a>facebook.com</a><p><a url=\"www.google.com\">google</a><b>Is paying</b><a url=\"www.reddit.com\">reddit</a></p></p>"
    self.assertEqual(parent_node2.to_html(),assert_str)
  
  def test_no_child(self):
    parent_node = ParentNode("a",None)
    self.assertRaises(ValueError)