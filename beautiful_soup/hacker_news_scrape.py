from operator import index
from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
title_links = soup.find_all(name="a", class_="titlelink")

article_tuple_title_link = []
for title_link in title_links:
    article_tuple_title_link.append((title_link.getText(), title_link.get("href")))

votes_for_articles = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

max_vote = votes_for_articles.index(max(votes_for_articles))
print(article_tuple_title_link[max_vote][0])
print(article_tuple_title_link[max_vote][1])
print(max(votes_for_articles))