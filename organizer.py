import os
import shutil
import argparse

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Programs": [".exe", ".msi"],
    "Code": [".py", ".js", ".cpp", ".c", ".java", ".html", ".css"]
}

def find_empty_folders(folder_path):
    empty_folders = []

    for root, dirs, files in os.walk(folder_path):
        if root == folder_path:
            continue
        if not dirs and not files:
            empty_folders.append(root)

    return empty_folders

def organize_files(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            ext = ext.lower()

            moved = False
            for folder_name, extensions in FILE_TYPES.items():
                if ext in extensions:
                    target_folder = os.path.join(folder_path, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, file))
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, file))

def main():
    parser = argparse.ArgumentParser(description="Smart File Organizer")
    parser.add_argument(
        "path",
        nargs="?",
        default=os.getcwd(),
        help="Folder path to organize (default: current directory)"
    )

    args = parser.parse_args()

    # Find empty folders FIRST
    empty_folders = find_empty_folders(args.path)

    if empty_folders:
        print("📂 Empty folders found (listed first):")
        for folder in empty_folders:
            print(f" - {folder}")
        print()  # spacing

    organize_files(args.path)
    print("✅ Files organized successfully!")

if __name__ == "__main__":
    main()
