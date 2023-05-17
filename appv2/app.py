from typing import List


def find_duplicate_feeds(file_path: str) -> List[str]:
    with open(file_path, "r") as f:
        feeds = [line.strip() for line in f.readlines()]

    duplicates = []
    for feed in set(feeds):
        if feeds.count(feed) > 1:
            duplicates.append(feed)

    return duplicates


if __name__ == "__main__":
    feeds_file = "feedly-merged.opml"
    duplicates = find_duplicate_feeds(feeds_file)

    with open("duplicates.txt", "w") as f:
        for duplicate in duplicates:
            f.write(f"{duplicate}\n")
