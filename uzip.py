# Description: Unzip a file and move it to a new folder with a new name and the date and time of the unzipping then
# then delete the original zip file

# TODO: Add a GUI with TKinter and TkinterCustom
# TODO: Make it possibble to unzip multiple files at once.

import os
import zipfile
import shutil
from datetime import datetime
import tkinter
import customtkinter

# System Settings
customtkinter.set_appearance_mode("sumary_line")
customtkinter.set_default_color_theme("blue")

# Create the main window/app frame
app = customtkinter.CTk()
app.geometry('720x480')
app.title('Uzip')

# App main loop
app.mainloop()

# TODO: Remove hard coded path
# navigate to the download folder
download_folder = 'C:\\Users\\Bligh\\Documents\\unziptest\\'  # Add your own path here
os.chdir(download_folder)

print('Navigated to the download folder')

# find all zipfiles in the download folder
zipfiles = [file for file in os.listdir() if file.endswith('.zip')]

print('Found all zip files in the download folder')

# extract the files from each zipfile
for zip_file in zipfiles:
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall()
    except zipfile.BadZipFile:
        print(f'{zip_file} is not a valid zip file')

print('Extracted all files from the zip files')

folder_name = None

# iterate over the extracted files
for file in os.listdir():
    if os.path.isfile(file) and not file.endswith('.zip'):
        if folder_name is None:
            current_date = datetime.now().strftime('%Y-%m-%d')
            folder_name = f'Extracted-{current_date}'
            os.mkdir(folder_name)
            open(f'{folder_name}/info.txt', 'a').close()
        shutil.move(file, f'{folder_name}/{file}')
        print(f'Moved {file} to {folder_name}')
    if os.path.isfile(file) and file.endswith('.zip'):
        os.remove(file)
        print(f'Deleted {file}')

print('Moved all files to a new folder and deleted the original zip files')
print('Done')
