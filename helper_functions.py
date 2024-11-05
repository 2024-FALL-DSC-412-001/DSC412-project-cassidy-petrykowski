import os
from PIL import Image

#Calculates the average image size in a directory.
def get_average_image_size(directory):
    

    total_width = 0
    total_height = 0
    image_count = 0

    for subdir, files in os.walk(directory):
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


width, height = get_average_image_size('/home/cassidy/DSC412/project/DSC412-project-cassidy-petrykowski/data/photos')

print(width, height)
# citation