import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)
  
  def test_noteq(self):
    node = TextNode("This is a text nod", TextType.NORMAL)
    node2 = TextNode("This is a text nod", TextType.BOLD)
    self.assertNotEqual(node,node2)
  
  def test_eq2(self):
    node = TextNode("This is a text nod", TextType.NORMAL,"www.google.com")
    node2 = TextNode("This is a text nod", TextType.NORMAL,"www.google.com")
    self.assertEqual(node,node2)


if __name__ == "__main__":
    unittest.main()