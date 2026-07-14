from operator import truediv

from PIL import Image
import numpy as np

im1 = Image.open("/Users/lapytopy/Desktop/其他/Archive/dolomite1/IMG_1758667067397.JPEG")
im1 = im1.convert("RGB")
im2 = Image.open("/Users/lapytopy/Desktop/其他/Archive/帅帅_Archive/米兰/IMG_2242.JPG")
im2 = im2.convert("RGB")

arr1 = np.array(im1)
arr2 = np.array(im2)
height_1 = arr1.shape[0]
width_1 = arr1.shape[1]
height_2 = arr2.shape[0]
width_2 = arr2.shape[1]

min_wdith = min(width_1, width_2)
min_height = min(height_1, height_2)

box1 = ((width_1 - min_wdith)/2, ((height_1 - min_height)/2), min_wdith + (width_1 - min_wdith)/2, min_height + ((height_1 - min_height)/2))
box2 = ((width_2 - min_wdith)/2, ((height_2 - min_height)/2), min_wdith + (width_2 - min_wdith)/2, min_height + ((height_2 - min_height)/2))

im1 = im1.crop(box1)
im2 = im2.crop(box2)

arr1 = np.array(im1)
arr2 = np.array(im2)
narr = np.zeros_like(im1)

# print(arr1.shape, arr2.shape)
# im1.show()
# im2.show()

def brightness_calculation(r,g,b):
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    if y >= 50:
        return True
    else:
        return False

for x in np.arange(arr1.shape[0]):
    for y in np.arange(arr1.shape[1]):
        pixel = arr1[x][y]
        r, g, b = pixel[0], pixel[1], pixel[2]
        if brightness_calculation(r, g, b):
            narr[x][y] = arr2[x][y]
        else:
            narr[x][y] = arr1[x][y]

output = Image.fromarray(narr)

output.show()

