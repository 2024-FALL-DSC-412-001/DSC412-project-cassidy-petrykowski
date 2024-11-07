# functions used for analysis and pre-processing

import os
from PIL import Image

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

def bgremove2(myimage):
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
    return finalimage