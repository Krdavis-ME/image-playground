# Coverts images with the JPG extension and saves them as PNG
# Takes 2 imputs from terminal
#   1. Folder Name of where the image is located
#   2. File name of the size that you want
#   3. File name of that you want to resize

# Terminal command example:
#   python JPGtoPNGConverter.py FolderName\ fileName.jpg fileName2.jpg
#   python JPGtoPNGConverter.py Pokedex\ pikachu.jpg bulbasaur.jpg


import sys                                                              #Importing System Module
import os                                                               #Importing OS Module
from PIL import Image                                                   #Importing Pillow Module

#Grabbing first and second parameters, Folder name and New folder name
folder_name = sys.argv[1]
file_name1 = sys.argv[2]                                               #Assigning first parameter(Orgin Folder) to folder_name
file_name2 = sys.argv[3]                                             #Assigning second parameter(New Folder or existing) to output_folder

#Check if new folder exists, if not create
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)


image1 = Image.open(f'{folder_name}{file_name1}')       #Stores the first image
image2 = Image.open(f'{folder_name}{file_name2}')       #Stores the Second image
image_size = image1.size                                #Grabs the size of the first image
print (image_size)
image_size2 = image2.size                               #Grabs the size of the second image
print (image_size2)
image2 = image2.resize((image_size), Image.LANCZOS)     #Resizes the second image to match the first
print (image2.size)
clean_name = os.path.splitext(file_name2)[0]
image2.save(f'{folder_name}{clean_name}-resize.jpg')    #Saving resized second image, preserving the original.