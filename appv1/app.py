import os
import xml.etree.ElementTree as ET

from typing import List


def get_feeds() -> List[str]:
    # Set the path to the folder containing the feed files. '..' indicates the parent directory of the current working directory.
    feed_files_folder = os.path.abspath("../feed-files")

    # Set the path to the 'feedly.opml' file inside the 'feed-files' folder.
    feedly_opml_path = os.path.join(feed_files_folder, "feedly.opml")

    # Open the 'feedly.opml' file for reading.
    with open(feedly_opml_path) as f:
        # Read the contents of the 'feedly.opml' file into a variable.
        feedly_opml_contents = f.read()
        # Parse the XML data in the 'feedly.opml' file and store the root element in a variable.
        feedly_root = ET.fromstring(feedly_opml_contents)

    # Set the path to the 'freshrss.opml.xml' file inside the 'feed-files' folder.
    freshrss_opml_path = os.path.join(feed_files_folder, "freshrss.opml.xml")

    # Open the 'freshrss.opml.xml' file for reading.
    with open(freshrss_opml_path) as f:
        # Read the contents of the 'freshrss.opml.xml' file into a variable.
        freshrss_opml_contents = f.read()
        # Parse the XML data in the 'freshrss.opml.xml' file and store the root element in a variable.
        freshrss_root = ET.fromstring(freshrss_opml_contents)

    all_feeds = []

    # Loop through all 'outline' elements with the 'type' attribute equal to 'rss' in the 'feedly.opml' file.
    for outline in feedly_root.findall(".//outline[@type='rss']"):
        # Append the XML data of the current 'outline' element to the list of all feeds.
        all_feeds.append(ET.tostring(outline).decode().strip())

    # Loop through all 'outline' elements with the 'type' attribute equal to 'rss' in the 'freshrss.opml.xml' file.
    for outline in freshrss_root.findall(".//outline[@type='rss']"):
        # Append the XML data of the current 'outline' element to the list of all feeds.
        all_feeds.append(ET.tostring(outline).decode().strip())

    return all_feeds
