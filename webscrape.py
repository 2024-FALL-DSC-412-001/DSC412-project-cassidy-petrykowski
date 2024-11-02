# script to scrape data from websites

# step: importing data

import hashlib
import io
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup
from pathlib import Path
from PIL import Image


options = ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

driver.get("https://www.braceletbook.com/patterns/alpha/159657/")
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
driver.quit()

def gets_url(classes, location, source, lake):
    results = []
    for a in lake.findAll(attrs={"class": classes}):
        name = a.find(location)
        if name not in results:
            results.append(name.get(source))
    return results


def get_grids(b_soup):
    returned_results = gets_url("preview_svg", "img", "src", b_soup)
    print(returned_results)
    for b in returned_results:
        image_content = requests.get(b).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert("RGB")
        file_path = Path("/home/cassidy/DSC412/project/DSC412-project-cassidy-petrykowski/data/grids", hashlib.sha1(image_content).hexdigest()[:10] + ".png")
        image.save(file_path, "PNG", quality=80)

def get_photos(b_soup):
    returned_results = gets_url("photos_item", "img", "src", b_soup)
    print(returned_results)
    for b in returned_results:
        image_content = requests.get(b).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert("RGB")
        file_path = Path("/home/cassidy/DSC412/project/DSC412-project-cassidy-petrykowski/data/photos", hashlib.sha1(image_content).hexdigest()[:10] + ".png")
        image.save(file_path, "PNG", quality=80)

if __name__ == "__main__":
    get_grids(soup)
    get_photos(soup)

# take url to one specific pattern

# take the gridded pattern(s)

# save to data/grids/<pattern number>/

# take the photo(s) of the pattern

# save to data/photos/<pattern number>/


