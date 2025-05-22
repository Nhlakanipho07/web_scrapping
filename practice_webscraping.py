import sqlite
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films"

movies_db = "Movies.db"
table_name = "Top 25"
movies_df = pd.DataFrame(columns=["Film", "Year", "Rotten Tomatoes' Top 100"])
count = 0

html_page = requests.get(url).text
data = BeautifulSoup(html_page, "html.parse")
table = data.find_all("tbody")
rows = table[0].find_all("tr")

for row in rows:
  if count < 25:
    cells = row.find_all("td")
    if cells:
      data_dict = {
        "Film": cells[1].contents[0],
        "Year": cells[2].contents[0],
        "Rotten Tomatoes' Top 100": cells[3].contents[0]
      }
      temp_df = pd.DataFrame(data_dict, index=[0])
      movies_df = pd.concat([temp_df, movies_df], ignore_index=True)
      count += 1
    else:
      break
    
  filtered_movies = movies_df[movies_df["Year"].astype(int) >= 2000]
  print(filtered_movies)