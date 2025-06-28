import os
import shutil

DOWNLOADS_FOLDER = r"C:\Users\HP\Downloads"

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Audio': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Scripts': ['.py', '.js', '.sh']
}

def create_folder(folder_name):
    folder_path=os.path.join(DOWNLOADS_FOLDER,folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path


def move_file(file, destination_folder):
    try:
        shutil.move(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(destination_folder, file))
        print(f"Moved: {file} → {destination_folder}")
    except Exception as e:
        print(f"Error moving {file}: {e}")

def sort_files():
    for file in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, file)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            moved = False

            for folder, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    destination = create_folder(folder)
                    move_file(file, destination)
                    moved = True
                    break
            
            if not moved:
                other_folder = create_folder("Others")
                move_file(file, other_folder)

if __name__ == "__main__":
    sort_files()
    print("\n Folder organization completed.")
