import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/search/title/?release_date=2013-01-01,2023-01-01&sort=release_date,asc&count=250"
response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')
movie_elements = soup.find_all('div', class_='lister-item-content')
movie_data = []

for movie_element in movie_elements:
    try:
        title = movie_element.find('h3', class_='lister-item-header').a.text
        year = movie_element.find('span', class_='lister-item-year').text.strip('()')
        rating = movie_element.find('div', class_='inline-block ratings-imdb-rating').strong.text
        director_element = movie_element.find('p', class_='').find_all('a')
        if director_element:
            director = director_element[0].text
        else:
            director = "N/A"
        genre_elements = movie_element.find_all('span', class_='genre')
        genre = [g.text.strip() for g in genre_elements] if genre_elements else []

        movie_info = {
            'Movie Title': title,
            'Release Year': year,
            'IMDB Rating': rating,
            'Director': director,
            'Genre': genre
        }

        movie_data.append(movie_info)
    except Exception as e:
        print(f"Error processing a movie: {e}")

csv_filename = "imdb_movies.csv"

with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['Movie Title', 'Release Year', 'IMDB Rating', 'Director', 'Genre']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for movie_info in movie_data:
        writer.writerow(movie_info)


df = pd.read_csv('imdb_movies.csv')


def average_imdb_rating():
    return df['IMDB Rating'].astype(float).mean()


def common_genre():
    return df["Genre"].mode().values[0]


def highest_rating_director():
    director_average_ratings = df.groupby("Director")["IMDB Rating"].mean()
    director_highest_average_rating = director_average_ratings.idxmax()
    return director_highest_average_rating


def year_with_max_movies():
    return df["Release Year"].value_counts().idxmax()


print("Average IMDB rating for the top-rated movies: ", average_imdb_rating())
print("The most common genre among the top-rated movies: ", common_genre())
print("The director with the highest average IMDb rating: ", highest_rating_director())
print("The year with the highest number of top-rated movies: ", year_with_max_movies())
