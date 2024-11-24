# DSC412-project

Just for clarity--

"Pattern" refers to the design itself.

"Grid" refers to the gridden pattern used to make the design. This lives entirely in digital form and isn't a product.

"Photo" refers to the photos of physical knotwork (typically bracelets) based on the grids.

"Run" refers to a command run in terminal.

## Virtual Environment

The first step is to create a virtual environment.

To create the virtual environment, run:

`python -m venv .venv`

To source the virtual environment (in Linux), run the following command or the equivalent in other operating systems:

`source .venv/bin/activate`

Then run `pip install -r requirements.txt`

Alternatively, create a virtual environment through VS Code, using requirements.txt to install the requirements through the system.

## Gathering Data

#### Webscraper

The webscraper goes through https://www.braceletbook.com/photos/ page by page and takes the URLs of each pattern, taking only "alpha"
and "normal" patterns. "Alpha" patterns are one-sided, while "normal" patterns are double sided, but that only impacts the execution
of the knotwork, NOT the generation of grids or this project (to my current understanding). The webscraper then takes photos of the 
patterns and the grids used to create them from each pattern's associated URL.

Some code was taken from https://oxylabs.io/blog/scrape-images-from-website.

To run in terminal:

`python3 webscraper.py`

## Model

#### To run:

Iterate through the training.ipynb file. Be sure to go in order, as the imports precede the sections, and contain critical functions from
helper_function.py.

Work through each step until the running the training loop. This step will take 6 to 12 hours depending on your system set up.

After training the model, which you can view the progress of on the Tensorboard, you can restore the checkpoints and generate images to test
how well the model worked.









