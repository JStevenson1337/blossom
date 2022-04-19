from tkinter import image_names
from traceback import print_tb
import requests, lxml, re, json 
from bs4 import BeautifulSoup, ResultSet

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
print(example)



