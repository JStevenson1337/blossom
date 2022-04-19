import fileinput
import shutil
from tkinter import image_names
from traceback import print_tb
from turtle import screensize
import requests
import lxml
import re
import json
from bs4 import BeautifulSoup, ResultSet
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# import pandas as pd
# from IPython.display import Image, HTML

# https://towardsdatascience.com/a-tutorial-on-scraping-images-from-the-web-using-beautifulsoup-206a7633e948

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

html = requests.get("https://unsplash.com/s/photos/flowers")
#html = requests.get("https://www.google.com/search?q=flowers&tbm=isch&source=hp&biw=948&bih=952&ei=bKteYufDIoS4qtsP_IG5oAo&iflsig=AHkkrS4AAAAAYl65fP8neUwk2mlQr7kj0Lhw_6TUBNdE&ved=0ahUKEwjnqeXZkKD3AhUEnGoFHfxADqQQ4dUDCAc&uact=5&oq=flowers&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyCAgAEIAEELEDMgUIABCABDIICAAQgAQQsQMyCAgAEIAEELEDMgsIABCABBCxAxCDATIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQNQAFjkCWDtCmgAcAB4AIABhgGIAZYEkgEDNS4ymAEAoAEBqgELZ3dzLXdpei1pbWc&sclient=img")

IMGDIR = "static/images/"

def scrape_urls():
    soup = BeautifulSoup(html.text, "lxml")
    image_container = soup.find_all('img')
    example = image_container[0]
    example.attrs['src']
    FILE = open(os.path.join(IMGDIR, "images.txt"), "w")
    try:
        for image in image_container:
            FILE.write(image.attrs['src'] + "\n")
    except Exception as e:
        print(e)
    finally:
        FILE.close()

def show_images():
    with open(os.path.join(IMGDIR, "images.txt"), "r") as f:
        for line in f:
            print(line)
            try:
                response = requests.get(line, stream=True)
                for chunk in response.iter_content(chunk_size=128):
                    with open(os.path.join(IMGDIR, "images.jpg"), "wb") as f:
                        f.write(chunk)
                        shutil.copyfileobj(response.raw, f)
                        image = mpimg.imread(line)
                        imgplot = plt.imshow(image)
                        plt.imshow(image)
            except Exception as e:
                print(e)
                continue


scrape_urls()
show_images()
print("Done")
