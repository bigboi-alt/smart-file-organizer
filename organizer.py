import os
import shutil
import argparse

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Code": [".py", ".js", ".cpp", ".c"]
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist!")
        return

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file_name)

        moved = False
        for folder, extensions in FILE_TYPES.items():
            if ext.lower() in extensions:
                dest_folder = os.path.join(folder_path, folder)
                os.makedirs(dest_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(dest_folder, file_name))
                moved = True
                break

        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, file_name))


def main():
    parser = argparse.ArgumentParser(description="Smart File Organizer")
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
