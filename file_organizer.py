
 #file_Organizer 

import os
import shutil

# Define file categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".apk"],
    "Others": []  # Anything not categorized
}

def organize_files(directory):
    """Organizes files in the specified directory into categorized folders."""
    
    if not os.path.exists(directory):
        print("Error: The directory does not exist.")
        return

    # Get all files in the directory
    files = os.listdir(directory)

    for file in files:
        file_path = os.path.join(directory, file)

        # Ignore folders, only process files
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()

            # Find the correct category for the file
            folder_name = "Others"  # Default category
            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    folder_name = category
                    break

            # Create category folder if it doesn't exist
            category_folder = os.path.join(directory, folder_name)
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

            # Move file to the correct folder
            shutil.move(file_path, os.path.join(category_folder, file))
            print(f"Moved: {file} → {folder_name}")

    print("\n✅ File organization complete!")

# Specify the folder you want to organize
folder_path = input("Enter the folder path to organize: ")
organize_files(folder_path)
