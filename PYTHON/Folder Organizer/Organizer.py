import os
import shutil

DOWNLOADS_PATH = os.path.join(os.path.expanduser("~"), "Downloads")

DIRECTORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".tar.gz", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
}

def organize_folder():
    if not os.path.exists(DOWNLOADS_PATH):
        print(f"The path {DOWNLOADS_PATH} does not exist.")
        return

    for filename in os.listdir(DOWNLOADS_PATH):
        file_path = os.path.join(DOWNLOADS_PATH, filename)

        if os.path.isdir(file_path):
            continue  # Skip directories

        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        for  folder_name, extensions in DIRECTORIES.items():
            if extension in extensions:
                target_folder = os.path.join(DOWNLOADS_PATH, folder_name)

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved {filename} to {target_folder}")
                break

if __name__ == "__main__":
    print("Organizing files in the Downloads folder...")
    organize_folder()
    print("Organization complete.")