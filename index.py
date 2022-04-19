import fileinput
import shutil
from tkinter import image_names
from traceback import print_tb
import requests, lxml, re, json 
from bs4 import BeautifulSoup, ResultSet
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
from IPython.display import Image, HTML


headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

# https://serpapi.com/playground?q=Flowers&tbm=isch&ijn=0
params = {
    "q": "Flowers",
    "tbm": "isch",
    "ijn": "0",
}

html = requests.get("https://unsplash.com/s/photos/flowers")
soup = BeautifulSoup(html.text, "lxml")
image_container = soup.find_all('img')
example = image_container[0]
example.attrs['src']
FILE = open("images.txt", "w")
try:
    for image in image_container:
        FILE.write(image.attrs['src'] + "\n")
except Exception as e:
    print(e)
finally:
    FILE.close()


with open("images.txt", "r") as f:
    for line in f:
        print(line)
        try:
            response = requests.get(line, stream=True)
            while line:
                line = response.raw.read(1024)
                with open(line, "wb") as f:
                    shutil.copyfileobj(response.raw, f)
                    image = mpimg.imread(line)
                    imgplot = plt.imshow(image)
                    plt.imshow(image)
        except Exception as e:
            print(e)
        finally:
            del response

print("Done")





