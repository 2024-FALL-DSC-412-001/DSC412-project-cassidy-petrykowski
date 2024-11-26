# functions used for analysis and pre-processing

import os
from PIL import Image
import math

#Calculates the average image size in a directory.
def get_average_image_size(directory):
    

    total_width = 0
    total_height = 0
    image_count = 0

    for subdir, dir, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(subdir, file)
            print(filepath)
            with Image.open(filepath) as img:
                width, height = img.size
                total_width += width
                total_height += height
                image_count += 1

    if image_count == 0:
        return (0, 0)

    average_width = total_width // image_count
    average_height = total_height // image_count
    return (average_width, average_height)


import numpy as np
import cv2 as cv2
from matplotlib import pyplot as plt

def bgremove2(img_path):
    myimage = cv2.imread(img_path)
    # First Convert to Grayscale
    myimage_grey = cv2.cvtColor(myimage, cv2.COLOR_BGR2GRAY)
 
    ret,baseline = cv2.threshold(myimage_grey,127,255,cv2.THRESH_TRUNC)
 
    ret,background = cv2.threshold(baseline,126,255,cv2.THRESH_BINARY)
 
    ret,foreground = cv2.threshold(baseline,126,255,cv2.THRESH_BINARY_INV)
 
    foreground = cv2.bitwise_and(myimage,myimage, mask=foreground)  # Update foreground with bitwise_and to extract real foreground
 
    # Convert black and white back into 3 channel greyscale
    background = cv2.cvtColor(background, cv2.COLOR_GRAY2BGR)
 
    # Combine the background and foreground to obtain our final image
    finalimage = background+foreground
    cv2.imwrite(img_path,finalimage)
    
def showimage(myimage):
    if (myimage.ndim>2):  #This only applies to RGB or RGBA images (e.g. not to Black and White images)
        myimage = myimage[:,:,::-1] #OpenCV follows BGR order, while matplotlib likely follows RGB order
         
    fig, ax = plt.subplots(figsize=[5,5])
    ax.imshow(myimage, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()   


# FIGURE OUT HOW TO MERGE IMAGES SO THAT THE INPUT IS ACCEPT BY PIX2PIX
def merge_images(grid_path, photo_path, path):

    # Open the images
    left = Image.open(grid_path)
    right = Image.open(photo_path)

    # Create a new image with the combined width and height
    width = left.width + right.width
    height = max(left.height, right.height)
    merged_image = Image.new("RGBA", (width, height))

    # Paste the first image
    merged_image.paste(left, (0, 0))

    # Paste the second image next to the first one
    merged_image.paste(right, (left.width, 0))

    # Save the merged image
    final_file_path = path + os.path.basename(right.filename)
    merged_image.save(final_file_path) 

    return final_file_path

# making a square around image that is too large

def shrink_and_square(im, width, height, target_size=218, fill_color=(255, 255, 255, 255)):
    # print("before width: " + str(width))
    # print("before height: " + str(height))
    ratio = target_size/height
    new_width = int(width * ratio)
    if (new_width % 2):
        new_width += 1
    resized_img = im.resize((new_width, target_size))
    if resized_img.width <= target_size:
         return resized_img  # No need to crop
    trim_pixels = (new_width - target_size) / 2
    top = 0
    bottom = target_size
    left = trim_pixels
    right = new_width - trim_pixels

    cropped_img = resized_img.crop((left, top, right, bottom))

    return cropped_img
    
    # im.thumbnail((target_size, target_size))
    # new_im = Image.new('RGBA', (target_size, target_size), fill_color)
    # new_im.paste(im)
    # return new_im