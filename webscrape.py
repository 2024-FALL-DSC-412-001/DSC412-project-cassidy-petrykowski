# importing data

# code partially taken from https://oxylabs.io/blog/scrape-images-from-website

import hashlib
import io
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup
from pathlib import Path
from PIL import Image
import os

def get_content_from_url(url):
    options = ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    page_content = driver.page_source
    driver.quit()
    return page_content

def parse_image_urls(content, classes, location, source):
    soup = BeautifulSoup(content, "html.parser")
    results = []
    for a in soup.findAll(attrs={"class": classes}):
        name = a.find(location)
        if name not in results:
            results.append(name.get(source))
    return results

def save_urls_to_csv(image_urls):
    df = pd.DataFrame({"links": image_urls})
    df.to_csv("links.csv", index=False, encoding="utf-8")

def get_and_save_image_to_file(image_url, output_dir):
    image_content = requests.get(image_url).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file).convert("RGB")
    filename = hashlib.sha1(image_content).hexdigest()[:10] + ".png"
    file_path = output_dir / filename
    image.save(file_path, "PNG", quality=80)

def get_name(image_url):
    image_content = requests.get(image_url).content
    name = hashlib.sha1(image_content).hexdigest()[:10]
    return name

def mkdir(name, folder):
    os.mkdir("data/" + folder + name)

def get_grids(url, name):
    mkdir(name, "grids/")
    content = get_content_from_url(url)
    image_urls = parse_image_urls(
        content=content, classes="preview_svg", location="img", source="src"
    )

    for image_url in image_urls:
        get_and_save_image_to_file(
            image_url, output_dir=Path("/home/cassidy/DSC412/project/DSC412-project-cassidy-petrykowski/data/grids/" + name + "/")
        )

def get_photos(url, name):
    mkdir(name, "photos/")
    content = get_content_from_url(url)
    image_urls = parse_image_urls(
        content=content, classes="photos_item", location="img", source="src"
    )

    for image_url in image_urls:
        get_and_save_image_to_file(
            image_url, output_dir=Path("/home/cassidy/DSC412/project/DSC412-project-cassidy-petrykowski/data/photos/" + name + "/")
        )

def scrape_pattern(url):
    name = get_name(url)
    get_grids(url, name)
    get_photos(url, name)

if __name__ == "__main__":

    
    url = "https://www.braceletbook.com/patterns/alpha/159657/"
    scrape_pattern(url)
    print("Done!")    

# take url to one specific pattern

# take the gridded pattern(s)

# save to data/grids/<pattern number>/

# take the photo(s) of the pattern

# save to data/photos/<pattern number>/


