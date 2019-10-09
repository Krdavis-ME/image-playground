from PIL import Image, ImageFilter
# Importing the Pillow Package and its modules: https://pillow.readthedocs.io/en/stable/index.html

# Creating variable to allow easier manipulation of the image
img = Image.open(f"./Pokedex/pikachu.jpg")

#filtered_img = img.filter(ImageFilter.BLUR)
#filtered_img.save("blur.png", 'png')
#filtered_img.show()
#convert_img = img.convert('L')

img.show()
# .format tell the format of the image. Ex (.jpg, .png)
# print(img.format)
# # .size tells the size of the image, in pixels
# print(img.size)
# # .mode tells the color scheme of the image
# print(img.mode)