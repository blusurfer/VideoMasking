from PIL import Image, ImageOps
import numpy as np

im1 = Image.open("/Volumes/Jerry's disk/Projects/VideoMasking/src/images/GjhuAilbYAAU-YC.jpeg")
im1 = im1.convert("RGB")
im2 = Image.open("/Volumes/Jerry's disk/Projects/VideoMasking/src/images/O1CN01HR6nff1zDwnCPlNUd_!!193306681.jpg")
im2 = im2.convert("RGB")
mask = Image.open("/Volumes/Jerry's disk/Projects/VideoMasking/src/images/GL. 2021-08-08 19.31.08.jpeg")
mask = mask.convert("RGB")


def merge_images(img1, img2, mask_img, effect):
    img1 = ImageOps.fit(img1, mask_img.size, centering=(0.5, 0.5))
    img2 = ImageOps.fit(img2, mask_img.size, centering=(0.5, 0.5))
    arr1 = np.array(img1)
    arr2 = np.array(img2)
    mask_arr = np.array(mask_img)
    canvas = np.zeros_like(mask_img)

    for x in np.arange(mask_arr.shape[0]):
        for y in np.arange(mask_arr.shape[1]):
            pixel = mask_arr[x][y]
            r, g, b = pixel[0], pixel[1], pixel[2]
            if effect(r, g, b):
                canvas[x][y] = arr2[x][y]
            else:
                canvas[x][y] = arr1[x][y]

    return Image.fromarray(canvas)


def brightness_calculation(r,g,b):
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    if y >= 150:
        return True
    else:
        return False


merge_images(im1, im2, mask, brightness_calculation).show()