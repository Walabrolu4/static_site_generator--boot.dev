from htmlnode import HTMLNode
class ParentNode(HTMLNode):
  def __init__(self,tag,children,props ={}):
    super().__init__(tag,None,children,props)

  def to_html(self):
    if self.tag is None:
      raise ValueError("No tag present")
    if self.children is None:
      raise ValueError("No Children present, Use a leaf node instead")
    
    formatted_string = f"<{self.tag}>"
    for child in self.children:
      formatted_string += child.to_html()
    formatted_string += f"</{self.tag}>"
    return formatted_string

    