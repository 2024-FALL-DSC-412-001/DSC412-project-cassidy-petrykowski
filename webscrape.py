# importing AND organizing the data

# code partially taken from https://oxylabs.io/blog/scrape-images-from-website

# scrapes https://www.braceletbook.com/photos/

import csv
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
from helper_functions import *
import time

storage_path = "/home/cassidy/DSC412/project/DSC412-project-cassidy-petrykowski/data"
new_width = 256
new_height = 256
#storage_path = "/media/cassidy/'Extreme SSD'/data"

# as it says
def get_content_from_url(url):
    options = ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    page_content = driver.page_source
    driver.quit()
    return page_content

# find location of pattern url
def parse_pattern_urls(content, classes, location, source):
    soup = BeautifulSoup(content, "html.parser")
    results = []
    for a in soup.findAll(attrs={"class": classes}):
        name = a.find(location)
        if name not in results:
            results.append(name.get(source))
    return results

# grab the image; save it to a file
def get_and_save_image_to_file(image_url, output_dir, isGrid=False, isFileName=False):
    image_content = requests.get(image_url).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file).convert("RGB")
    if isGrid:
        image = shrink_and_square(image, image.width, image.height)
    image = image.resize((new_width,new_height))
    filename = hashlib.sha1(image_content).hexdigest()[:10] + ".png"
    file_path = output_dir / filename
    image.save(file_path, "PNG", quality=80)
    if isFileName:
        return file_path, filename
    else:
        return file_path

# gets the name of the photo to use as folders and match up with 
def get_name(image_url):
    image_content = requests.get(image_url).content
    name = hashlib.sha1(image_content).hexdigest()[:10]
    return name

def mkdir(name, folder):
    os.mkdir("data/" + folder + name)

# take the gridded pattern(s)
def get_grids(url, name):
    mkdir(name, "grids/")
    content = get_content_from_url(url)
    image_urls = parse_pattern_urls(
        content=content, classes="preview_svg", location="img", source="src"
    )

    # save to data/grids/<pattern number>/
    for image_url in image_urls:
        grid_path = get_and_save_image_to_file(
            image_url, output_dir=Path(storage_path + "/grids/" + name + "/"), isGrid=True
        ) # technically grid_path gets rewritten everytime; the only reason this is okay for now is because this loop only ever runs once
    return grid_path

# take the photo(s) of the pattern
def get_photos(url, grid_path, name):
    mkdir(name, "photos/")
    content = get_content_from_url(url)
    image_urls = parse_pattern_urls(
        content=content, classes="photos_item", location="img", source="src"
    )

    # save to data/photos/<pattern number>/
    for image_url in image_urls:
        photo_path, merged_name = get_and_save_image_to_file(
            image_url, output_dir=Path(storage_path + "/photos/" + name + "/"), isFileName=True
        )
        merge_images(grid_path,photo_path, (storage_path + "/merged/"))
        save_items_to_csv(storage_path + "/merged/" + merged_name,"patterns")
    

# saves items to a csv
def save_items_to_csv(items, csv_name):
    with open("data/" + csv_name + '.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([items])
        f.close()

# scrapes an individual pattern page
def scrape_pattern(url):
    name = get_name(url)
    print(name)
    grid_path = get_grids(url, name)
    get_photos(url, grid_path, name)
    get_photos(url, grid_path, name)
    

# gets all the pattern page urls from the photos page
def get_page_urls(url):
    content = get_content_from_url(url)
    pumpkin_soup = BeautifulSoup(content, "html.parser")
    urls = []
    for link in pumpkin_soup.find_all(href=lambda href: href and (("normal" in href) or ("alpha" in href))):
        urls.append(link['href'])
    return urls

# gets all the urls from one page and scrapes them
def scrape_page(path):
    page_urls = get_page_urls(path)
    for url in page_urls:
        #print(url)
        scrape_pattern(url)

if __name__ == "__main__":
    # get the pattern page urls
    original_path = "https://www.braceletbook.com/photos/page-"
    for i in range(1,300):
        scrape_page(original_path + str(i) + '/')
        print("Page " + str(i) + " scraped!")
        # os.system("rm -rf data/grids/* data/photos/*")
        # time.sleep(20)

    print("Done!")    


