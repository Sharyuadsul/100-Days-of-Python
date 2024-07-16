import requests
from bs4 import BeautifulSoup

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup)

all_titles = soup.find_all(name="a", class_ = "storylink")
# print(all_titles.getText())
article_text = []
article_links = []

for article in all_titles:
    text = article.getText()
    article_text.append(text)
    link = article.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_ = "score")]

# print(article_text)
# print(article_links)
# print(article_upvote)

max_vote = max(article_upvote)
max_vote_index = article_upvote.index(max_vote)
# print(max_vote_index)
print(article_text[max_vote_index])
print(article_links[max_vote_index])

