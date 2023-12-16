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
#Keeps track of rank
num=1

#Creates a list that can be used for the CSV file
data_list=[]
#Looks at each identity in the table under the first and second column
for row in top_20:
    artist=(row.find_all("td")[0].text)
    listeners=(row.find_all("td")[1].text)
    #Creates a dictionary that is presented to the user of the artist and number of listeners
    spotify_dic={
        "Rank "+str(num):artist,
        "Monly listeners":listeners
    }
    #Puts the dictionary into the list to be used for the csv 
    data_list.append(spotify_dic)
    #Adds to the ranking
    num=num+1
    print(spotify_dic) 
print("\n")

#Allows user to pick artist from the list to get to know more about
artist_choice=input("Enter the artist name as written exactly above to learn a little bit more about them ")

#Puts the selection into format that can be used as the wikipedia link
artist_link=artist_choice.replace(" ","_")

artist_page=requests.get("https://en.wikipedia.org/wiki/"+ artist_link)
artist_soup=BeautifulSoup(artist_page.text, "html.parser")

#Finds the first paragraph in the artists wikipedia page and prints it for the user
intro=artist_soup.find_all("p")[1].text
print("\n")
print(intro)

#Puts the data or the dictionary created with all the artists into a csv file as a data frame.
df = pd.DataFrame(data_list)
df.to_csv('spotify_data.csv', index=False)
print("\nCSV file 'spotify_data.csv' created successfully.")
 



