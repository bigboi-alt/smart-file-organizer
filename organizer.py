import os
import shutil
import argparse

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".js", ".cpp", ".c", ".java", ".html", ".css"]
}


def get_unique_path(destination):
    """
    Prevents overwriting files by adding _1, _2, etc.
    """
    base, ext = os.path.splitext(destination)
    counter = 1

    while os.path.exists(destination):
        destination = f"{base}_{counter}{ext}"
        counter += 1

    return destination


def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Error: Folder does not exist.")
        return

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file_name)
        ext = ext.lower()

        moved = False

        for category, extensions in FILE_TYPES.items():
            if ext in extensions:
                dest_folder = os.path.join(folder_path, category)
                os.makedirs(dest_folder, exist_ok=True)

                destination = os.path.join(dest_folder, file_name)
                destination = get_unique_path(destination)

                shutil.move(file_path, destination)
                moved = True
                break

        # If file type not matched
        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)

            destination = os.path.join(other_folder, file_name)
            destination = get_unique_path(destination)

            shutil.move(file_path, destination)


def main():
    parser = argparse.ArgumentParser(
        description="Smart File Organizer - Organize files by type"
    )

    parser.add_argument(
        "--path",
        type=str,
        required=True,
        help="Path of the folder to organize"
    )

    args = parser.parse_args()

    organize_files(args.path)
    print("✅ Files organized successfully!")


if __name__ == "__main__":
    main()
