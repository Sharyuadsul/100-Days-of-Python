from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup)
# print(soup.title)
# print(soup.title.name)
#
# print(soup.a)
# print(soup.li)

# print(soup.prettify())

all_anchor_tags  = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))

heading = soup.find(name="h1", id = "name")
# print(heading.getText())

# h3_heading = soup.find(name="h3", class_ = "heading")
# print(h3_heading.getText())
# print(h3_heading.name)
# print(h3_heading.get('class'))

h3_heading= soup.select_one(selector=".heading")
print(h3_heading)

name = soup.select_one(selector="#name")
print(name)

company_name = soup.select_one(selector="p a")
print(company_name)

