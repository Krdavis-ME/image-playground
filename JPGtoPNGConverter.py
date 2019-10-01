# Coverts images with the JPG extension and saves them as PNG
# Takes 2 imputs from terminal
#   1. Folder Name of where the image is located
#   2. Folder Name where you want the new PNG folders to be located

# Terminal command example:
#   python JPGtoPNGConverter.py FolderName\ NewFolderName\
#   python JPGtoPNGConverter.py Pokedex\ PNGImages\


import sys                                                              #Importing System Module
import os                                                               #Importing OS Module
from PIL import Image                                                   #Importing Pillow Module

#Grabbing first and second parameters, Folder name and New folder name
folder_name = sys.argv[1]                                               #Assigning first parameter(Orgin Folder) to folder_name
output_folder = sys.argv[2]                                             #Assigning second parameter(New Folder or existing) to output_folder

print(folder_name, output_folder)
#Check if new folder exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through folder
# convert images to png
# save to the new folder
for filename in os.listdir(folder_name):                                #filename is local variable that stores each file from folder_name(Orgin Folder)
    image = Image.open(f'{folder_name}{filename}')                      #image stores the image for manipulation
    clean_name = os.path.splitext(filename)[0]                          #clean_name stores the file's name without its extension
    image.save(f'{output_folder}{clean_name}.png', 'png')               #Saving the filename to Output foler with extension '.png'
    print('Image Converted!')
