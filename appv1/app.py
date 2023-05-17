import os
import xml.etree.ElementTree as ET

feed_files_folder = os.path.abspath("../feed-files")

feedly_opml_path = os.path.join(feed_files_folder, "feedly.opml")
with open(feedly_opml_path) as f:
    feedly_opml_contents = f.read()

freshrss_opml_path = os.path.join(feed_files_folder, "freshrss.opml.xml")
with open(freshrss_opml_path) as f:
    freshrss_opml_contents = f.read()

# if feedly_opml_contents and freshrss_opml_contents:
#     print("Both OPML files were read successfully.")
