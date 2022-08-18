from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
movie_content = response.text

soup = BeautifulSoup(movie_content, "html.parser")
all_movies = soup.find_all(name="h3", class_="jsx-4245974604")
print(all_movies)