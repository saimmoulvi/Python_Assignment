"""
importing os for operating system operations
importing sys for accessing command line arguments
importing shutil to provide high level operations on files and directories
importing datetime for generating timestamps to ensure unique filenames
"""

import os
import sys
import shutil
from datetime import datetime

def file_backup(source_directory, destination_directory):
    #checking if the file name already exists
    if not os.path.exists(source_directory):
        print (f"Error: Source directory '{source_directory}' does not exist.")
        return
    
    # Creating destination directory if it doesn't exist
    os.makedirs(destination_directory, exist_ok=True)
        
    #getting list of files in source directory
    files = os.listdir(source_directory)

    for file in files:
        source_file = os.path.join(source_directory, file)
        dest_file = os.path.join(destination_directory, file)

        #Checking if destination file already exists
        if os.path.exists(dest_file):
            #Appending a timestamp to make the filename unique
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            filename, file_extension = os.path.splitext(file)
            new_filename = f"{filename}_{timestamp}{file_extension}"
            dest_file = os.path.join(destination_directory, new_filename)

        # Copying the file from source to destination
        try:
            shutil.copy2(source_file, dest_file)
            print(f"Successfully copied '{source_file}' to '{dest_file}'")
        except Exception as e:
            print(f"Error: Failed to copy '{source_file}' to '{dest_file}' : {e}")

if __name__ == "__main__":
    #Checking if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("python backup.py /path/to/source /path/to/destination")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    file_backup(source_directory, destination_directory)                  
