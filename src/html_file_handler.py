import os
import shutil
from html_transformer import markdown_to_html_node

def delete_public():
  print("Deleting all from public \n")
  if(os.path.exists("./public")):
    shutil.rmtree("./public")
  os.mkdir("./public")


def copy_static_to_public():
  delete_public()
  copy_all_files("./static","./public")

def copy_all_files(source,destination):
  for file in os.listdir(source):
    joined_path = os.path.join(source,file)
    print(joined_path)
    if os.path.isfile(joined_path):
      print()
      print(f"copying {file} from {joined_path} to {destination}")
      shutil.copy(joined_path,destination)
    else:
      new_folder = os.path.join(destination,file)
      print(f"Creating folder {new_folder}")
      os.mkdir(new_folder)
      copy_all_files(joined_path,new_folder)

def extract_title(markdown):
  markdown = markdown.split("\n\n")
  for line in markdown:
    if line[:2] == "# ":
      line = line[2:]
      line = line.strip()
      if len(line) == 0:
        raise Exception("Title found but is empty")
      return(line)
  raise Exception("Title not found")

def generate_page(from_path,template_path,dest_path):
  print(f"generating page from {from_path} to {dest_path} using {template_path}")

  with open(from_path,'r') as f:
    markdown_text = f.read()

  with open(template_path,'r') as f:
    template = f.read()    


  html_nodes = markdown_to_html_node(markdown_text)

  html_text = html_nodes.to_html()
  title = extract_title(markdown_text)
  title_tag = "{{ Title }}"
  content_tag = "{{ Content }}"
  template = template.replace(title_tag,title)
  template = template.replace(content_tag,html_text)
  dest_dir = os.path.dirname(dest_path)
  #print(template)
  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

  with open(dest_path,"w") as f:
    f.write(template)
