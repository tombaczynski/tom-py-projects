# rename_txt_to_md.py
# It will change the file extension of all .txt files in the indicated directory to .md

import tkinter as tk
from tkinter import filedialog
import os

def rename_txt_to_md():
    """
    Opens a Windows system dialog for the user to select a folder.
    Then renames all files in that folder with a .txt by changing their extension to .md.
    It the user cancels the folder selection, the function exits without making any changes.
    
    Note:
        - Only files directly inside the selected folder are processed (no recursion).
        - Files are renamed in place.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    folder_path = filedialog.askdirectory(title="Select Folder with .txt Files")
    print(f"Selected folder: {folder_path}")
    
    if folder_path:
        # Iterate through all files in the selected directory
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                # Construct full file path
                old_file = os.path.join(folder_path, filename)
                new_file = os.path.join(folder_path, filename[:-4] + '.md')
                # Rename the file
                os.rename(old_file, new_file)
                print(f'Renamed: {old_file} to {new_file}')
    else:
        print("No folder selected. Exiting.")

def main():
    rename_txt_to_md()

if __name__ == "__main__":
    main()