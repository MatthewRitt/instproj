from bs4 import BeautifulSoup 
import pandas as pd 
import requests

# Requesting page with table we are going to scrape
spotify_page = requests.get("https://kworb.net/spotify/listeners.html")

# Parse the HTML content
spotify_soup = BeautifulSoup(spotify_page.content, "html.parser")

# Find the table and all rows (tr) inside the tbody
spotify_table = spotify_soup.find("table", {"class": "addpos sortable"}).find("tbody").find_all("tr")

# Shrinks the table to the top 20 rows
top_20 = spotify_table[:20]

# List to store the data for CSV
data_list = []

# Loop through each row and extract the artist and listeners
for num, row in enumerate(top_20, start=1):
    artist = row.find_all("td")[0].text.strip()
    listeners = row.find_all("td")[1].text.strip()

    # Create a dictionary for each artist and listeners for the csv file 
    spotify_dic = {
        "Rank": num,
        "Artist": artist,
        "Monthly Listeners": listeners
    }

    # Append to the data list
    data_list.append(spotify_dic)
    print(spotify_dic)

# Allow user to choose an artist to learn more about
artist_choice = input("Enter the artist name as written exactly above to learn a little bit more about them: ")

# Format the artist name for the Wikipedia link
artist_link = artist_choice.replace(" ", "_")

# Request the Wikipedia page for the artist
artist_page = requests.get("https://en.wikipedia.org/wiki/" + artist_link)
artist_soup = BeautifulSoup(artist_page.text, "html.parser")

# Find the first paragraph and display it
intro = artist_soup.find_all("p")[1].text
print("\n", intro)

# Convert the list of dictionaries into a DataFrame
df = pd.DataFrame(data_list)

# Save the data to a CSV file
df.to_csv('spotify_data.csv', index=False)
print("\nCSV file 'spotify_data.csv' created successfully.")
 



