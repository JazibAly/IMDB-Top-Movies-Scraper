# IMDb Top-Rated Movies Scraper

This Python script uses **BeautifulSoup** and **Requests** to scrape data from IMDb about top-rated movies released between **2013 and 2023**. It saves the results to a CSV file and performs several basic data analysis tasks using **Pandas**.

## 📌 Features

The script performs the following tasks:

### 🔍 Web Scraping
- Scrapes data from: [IMDb](https://www.imdb.com/search/title/?release_date=2013-01-01,2023-01-01&sort=release_date,asc&count=250)
- Extracts the following information for each movie:
  - Movie Title
  - Release Year
  - IMDb Rating
  - Director
  - Genre

### 📊 Data Storage
- Stores scraped data in a structured format using a **CSV file** (`imdb_movies.csv`).

### 📈 Data Analysis
- **Average IMDb Rating**: Calculates the average rating of all movies.
- **Most Common Genre**: Determines the most frequent genre among top-rated movies.
- **Top Director**: Identifies the director with the highest average IMDb rating.
- **Peak Year**: Finds the year with the highest number of top-rated movies.

## 🛠️ Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `pandas`

Install the required libraries using:

```bash
pip install requests beautifulsoup4 pandas
