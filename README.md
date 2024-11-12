# DSC412-project

Just for clarity--

"Pattern" refers to the design itself.

"Grid" refers to the gridden pattern used to make the design. This lives entirely in digital form and isn't a product.

"Photo" refers to the photos of physical knotwork (typically bracelets) based on the grids.

## Gathering Data

### Webscraper

The webscraper goes through https://www.braceletbook.com/photos/ page by page and takes the URLs of each pattern, taking only "alpha"
and "normal" patterns. "Alpha" patterns are one-sided, while "normal" patterns are double sided, but that only impacts the execution
of the knotwork, NOT the generation of grids or this project (to my current understanding). The webscraper then takes photos of the 
patterns and the grids used to create them from each pattern's associated URL.

Truthfully, this part was a learning curve.

Some code was taken from https://oxylabs.io/blog/scrape-images-from-website.

To run in terminal:

python3 webscraper.py

## Working on the model

To run:

Iterate through the training.ipynb file. Be sure to go in order, as the imports precede the sections, and contain critical functions from
helper_function.py.

### Analysis

Useful resource: https://www.datacamp.com/tutorial/seeing-like-a-machine-a-beginners-guide-to-image-analysis-in-machine-learning

Using thresholding to identify primary object in image. Using resources from OpenCV, https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html and https://www.freedomvc.com/index.php/2022/01/17/basic-background-remover-with-opencv/.

Also considering setting the colors in the image to a certain quanity, possibly based on information scraped from the website (i.e. how many colors are supposed to be in the pattern)

### Train/Test Split

The data is split 70% training, 30% test. The csv, patterns.csv holds all the codes for each pattern and allows you to find the associated
folder under either /photos or /grids.

### Model

#### Initial Plan

Data -> Resize and Normalize -> Confine to a certain number of colors -> isolate pattern within image and crop image to only include pattern

(not entirely sure how to do this step yet)

from there->image segmentation CNN finds the knots and grids them?

https://github.com/qubvel-org/segmentation_models.pytorch

#### Revised Plan







