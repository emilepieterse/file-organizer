import argparse
import os
import shutil

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".md", ".xlsx", ".csv", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}


def get_category(extension):
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Other"


def unique_destination(destination):
    """If destination already exists, append (1), (2), etc. to the filename."""
    if not os.path.exists(destination):
        return destination

    folder, name = os.path.split(destination)
    stem, extension = os.path.splitext(name)

    counter = 1
    while True:
        candidate = os.path.join(folder, f"{stem} ({counter}){extension}")
        if not os.path.exists(candidate):
            return candidate
        counter += 1


def organize_folder(folder_path, dry_run=False):
    if not os.path.isdir(folder_path):
        print(f"Folder not found: {folder_path}")
        return

    moved_count = 0

    for name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, name)

        if not os.path.isfile(full_path):
            continue

        extension = os.path.splitext(name)[1]
        category = get_category(extension)
        category_path = os.path.join(folder_path, category)
        destination = unique_destination(os.path.join(category_path, name))

        if dry_run:
            print(f"Would move {name} -> {category}/{os.path.basename(destination)}")
            moved_count += 1
            continue

        os.makedirs(category_path, exist_ok=True)

        try:
            shutil.move(full_path, destination)
            print(f"Moved {name} -> {category}/{os.path.basename(destination)}")
            moved_count += 1
        except Exception as e:
            print(f"Could not move {name}: {e}")

    verb = "Would organize" if dry_run else "Organized"
    print(f"\nDone. {verb} {moved_count} file(s).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort files in a folder into subfolders by type.")
    parser.add_argument("folder", help="Path to the folder to organize")
    parser.add_argument("--dry-run", action="store_true", help="Show what would move without moving anything")
    args = parser.parse_args()

    organize_folder(args.folder, dry_run=args.dry_run)
