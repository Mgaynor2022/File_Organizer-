import os
import shutil

directory = os.path.join(os.path.expanduser("~"), "Downloads", "Desktop")
destination_root = "/Users/mikeg"

extensions = {
    ".JPG": "Pictures",
    "jpg": "Pictures",
    ".jpeg": "Pictures",
    ".png": "Pictures",
    ".svg": "Pictures",
    ".gif": "Pictures",
    ".yaml": "Documents",
    ".html": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".pdf": "Documents",
    ".csv": "Documents",
    ".xlsx": "Documents",
    ".woff": "Documents",
    ".css": "Documents",
    ".mup": "Documents",
    ".json": "Documents"
    

}

for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file_name)[1]
        # Making all of the file_name lowercase. 

        if extension in extensions: 
            folder_name = extensions[extension]

            folder_path = os.path.join(destination_root, folder_name)
            os.makedirs(folder_path, exist_ok=True)  # Ensure the directory exists

            # Where we want the file to go.
            destination_path = os.path.join(folder_path, file_name)
            shutil.move(file_path, destination_path)

            print(f"Moved {file_name} to {folder_name} folder. ")
        else:
            print(f"Skipped {file_name}. Unknown file extension")
    else:
        print(f"Skipped {file_name}. It is a directory")

print("File Organizer Completed.")

