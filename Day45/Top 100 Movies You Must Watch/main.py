import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_titles = soup.find_all(name="h3", class_ = "title")

all_movies = [item.getText() for item in all_titles]
# print(all_movies)

movies=[]
for n in range(len(all_movies)-1, -1, -1):
    # print(all_movies[n])
    movies.append(all_movies[n])
# OR
# movies = all_movies[::-1]
# print(movies)

with open("movies.txt",mode="a", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")



