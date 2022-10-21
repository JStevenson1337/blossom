import fileinput
import shutil
from tkinter import image_names
from traceback import print_tb
from turtle import screensize
from defer import return_value
from numpy import source
import requests
from bs4 import BeautifulSoup, ResultSet
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from urllib.request import urlopen


# import pandas as pd
# from IPython.display import Image, HTML

# https://towardsdatascience.com/a-tutorial-on-scraping-images-from-the-web-using-beautifulsoup-206a7633e948

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

html = requests.get("https://unsplash.com/s/photos/flowers")

IMGDIR = "static/images/"
LOGDIR = "../logs/"

def log_images():
    pass

# has class but no ID
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

# Validating the images
def is_image(file):
    return file.endswith(".jpg" or ".png" or ".jpeg")

#TODO: Create a function to hash images and store them in a database
def hash_images(*image_hash):
    pass

def get_data(url):
    data = requests.get(url)
    soup = BeautifulSoup(htmldata, 'html, parser')
    for item in soup.find_all('img'):
        print(item['src'])
        
def store_images(image_url):
    with 


        # print(kwargs)
        # soup = BeautifulSoup(html.text, "lxml")
        # image_container = soup.find_all('img')
        # example = image_container[0]
        # example.attrs['src']
        # FILE = open(os.path.join(IMGDIR, "images.txt"), "w")
        # try:
        #     for image in image_container:
        #         FILE.write(image.attrs['src'] + "\n")
        # except Exception as e:
        #     print(e)
        # finally:
        #     FILE.close()


def show_images():
    count = 0

    with open(os.path.join(IMGDIR, "images.txt"), "r") as f:
        for line in f:
            try:
                img_data = requests.get(line, headers=headers)
                with open(os.path.join(IMGDIR, "%s-image.jpg" % count), "wb") as handler:
                    handler.write(img_data.content)
                count += 1
            except Exception as e:
                print(e)
                #print_tb(e)
                continue



int main():
    scrape_urls(True)
    show_images()

    return_value(0)


if __name__ == "__main__":
    main()


