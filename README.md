### DSC412-project

Just for clarity--

"Pattern" refers to the design itself.

"Grid" refers to the gridden pattern used to make the design. This lives entirely in digital form and isn't a product.

"Photo" refers to the photos of physical knotwork (typically bracelets) based on the grids.

## Gathering Data

# Webscraper

The webscraper goes through https://www.braceletbook.com/photos/ page by page and takes the URLs of each pattern, taking only "alpha"
and "normal" patterns. "Alpha" patterns are one-sided, while "normal" patterns are double sided, but that only impacts the execution
of the knotwork, NOT the generation of grids or this project (to my current understanding). The webscraper then takes photos of the 
patterns and the grids used to create them from each pattern's associated URL.

Truthfully, this part was a learning curve.

## Working on the model

# Train/Test Split

The data is split 70% training, 30% test. The csv, patterns.csv holds all the codes for each pattern and allows you to find the associated
folder under either /photos or /grids.

# 


