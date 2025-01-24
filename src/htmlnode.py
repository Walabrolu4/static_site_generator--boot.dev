class HTMLNode():
  def __init__(self,tag = None,value = None,children = None,props = None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError("Child must implement")
  
  def props_to_html(self):
    prop_string = ""
    for key,value in self.props.items():
      prop_string += f"{key}=\"{value}\""
    return prop_string

  def __repr__(self):
    repr = ""
    repr += (f"tag = {self.tag}\n")
    repr += (f"value = {self.value}\n")
    repr += (f"children = {self.children}\n")
    repr += (f"props = {self.props_to_html()}\n")
    return repr
