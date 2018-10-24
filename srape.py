import bs4
import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq



# Dealing with loggin stuff


form_data = {'username': 'myusername', 'pass': 'secretpassword'}
with requests.Session() as sesh:
    sesh.post(login_post_url, data=form_data)
    response = sesh.get(internal_url)
    html = response.text

soup = soup(html)    


my_url = "https://www.newegg.ca/Xbox-One-Systems/SubCategory/ID-3216?Tid=22812"

#opening connection and grabbing the page

uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html,"html.parser")

#grab the product
containers = page_soup.findAll("div", {"class":"item-container"})
