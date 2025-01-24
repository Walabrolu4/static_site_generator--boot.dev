from htmlnode import HTMLNode

class LeafNode(HTMLNode):
  def __init__(self,tag,value,props):
    super().__init__(tag,value,None,props)

  def to_html(self):
    if self.value is None:
      return ValueError ("all leaf nodes must gave a value!")
    if self.tag is None:
      return self.value
    if self.props is None:
      raw_html_string = f"<{self.tag}>{self.value}<\\{self.tag}>"
    else:
      raw_html_string = f"<{self.tag} {self.props_to_html()}>{self.value}<\\{self.tag}>"
    return raw_html_string  