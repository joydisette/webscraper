import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.ca/Xbox-One-Systems/SubCategory/ID-3216?Tid=22812"

#opening connection and grabbing the page

uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html,"html.parser")

#grab the product
containers = page_soup.findAll("div", {"class":"item-container"})
