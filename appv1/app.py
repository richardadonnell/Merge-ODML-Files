import os
import xml.etree.ElementTree as ET

feed_files_folder = os.path.abspath("../feed-files")

feedly_opml_path = os.path.join(feed_files_folder, "feedly.opml")
with open(feedly_opml_path) as f:
    feedly_opml_contents = f.read()

freshrss_opml_path = os.path.join(feed_files_folder, "freshrss.opml.xml")
with open(freshrss_opml_path) as f:
    freshrss_opml_contents = f.read()

# In the "feedly.opml" file, find the <body> tag. Under the <body> element, there are several <outline> elements. Print their text attribute contents of all <outline> elements.
tree = ET.ElementTree(ET.fromstring(feedly_opml_contents))
root = tree.getroot()

body = root.find("body")
outlines = body.findall("outline")

for index, outline in enumerate(outlines):
    outlines.sort(key=lambda x: x.get("text"))
    print(f"{index + 1}. {outline.get('text')}")

# In the "freshrss.opml.xml" file, find the <body> tag. Under the <body> element, there are several <outline> elements. Print their text attribute contents of all <outline> elements.
tree = ET.ElementTree(ET.fromstring(freshrss_opml_contents))
root = tree.getroot()

body = root.find("body")
outlines = body.findall("outline")

for index, outline in enumerate(outlines):
    outlines.sort(key=lambda x: x.get("text"))
    print(f"{index + 1}. {outline.get('text')}")
