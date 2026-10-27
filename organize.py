import os
import shutil
import sys

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


def organize_folder(folder_path):
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

        os.makedirs(category_path, exist_ok=True)

        destination = os.path.join(category_path, name)

        try:
            shutil.move(full_path, destination)
            print(f"Moved {name} -> {category}/")
            moved_count += 1
        except Exception as e:
            print(f"Could not move {name}: {e}")

    print(f"\nDone. {moved_count} file(s) organized.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python organize.py <folder_path>")
        sys.exit(1)

    organize_folder(sys.argv[1])
