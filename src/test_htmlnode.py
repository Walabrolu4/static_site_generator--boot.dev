import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
  def test_eq(self):
    html_node = HTMLNode('b',"hello",None,{"url":"www.google.com"})
    url = "url=\"www.google.com\" "
    self.assertEqual(html_node.props_to_html(),url)

  def test_eq2(self):
    html_node = HTMLNode('b',"hello",None,{"url":"www.google.com"})
    html_node2 = HTMLNode('b',"hello",None,{"url":"www.google.com"})
    self.assertEqual(html_node.__repr__(),html_node2.__repr__())
  
  def test_noteq(self):
    html_node = HTMLNode('b',"hello",None,{"url":"www.google.com"})
    html_node2 = HTMLNode('img',"hello",None,{"url":"www.google.com"})
    self.assertNotEqual(html_node.tag , html_node2.tag)

if __name__ == "__main__":
    unittest.main()
