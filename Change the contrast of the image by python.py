#Change the contrast of the image by python => pillow
# install: pip install Pillow
# from PIL import Image
# from  PIL import ImageEnhance

from PIL import Image
from  PIL import  ImageEnhance

image = input("Enter The Image : ")

# Open The Image
image = Image.open(image)

# show The old Image
image.show()

en = ImageEnhance.Contrast(image)
img = en.enhance(0.1)

# Save Image
img.save("result.jpg")

# show The new Image
img.show()
