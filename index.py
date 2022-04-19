import requests, lxml, re, json 
from bs4 import BeautifulSoup

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

html = requests.get("https://www.google.com/search", params=params, headers=headers)
soup = BeautifulSoup(html.text, 'lxml')
print(soup.prettify())

