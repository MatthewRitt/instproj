#Beautiful soup lets you scrape and navigate data on a html page
from bs4 import BeautifulSoup 
import numpy as np
import pandas as pd 

#Allows to grab the website to be able to scrape
import requests

#Requesting page with table we are going to scrape
spotify_page=requests.get("https://kworb.net/spotify/listeners.html")

#Parses through the html data and put its into a form that can be used in python and our code
spotify_soup=BeautifulSoup(spotify_page.content, "html.parser")

#I had to go onto the site and inspect the table to find the class associated with the table I was scraping
#Each artist is associated to a tr value within the t body so this is finding those values
spotify_table=spotify_soup.find("table", {"class":"addpos sortable"}).find("tbody").find_all("tr")
#Shrinks the table to 20 rows
top_20=spotify_table[:20]
num=1
for row in top_20:
    artist=row.find_all("td")[0].text
    listeners=row.find_all("td")[1].text
    spotify_dic={
        "Rank "+str(num):artist,
        "Monly listeners":listeners
    }
    num=num+1
    print(spotify_dic)


