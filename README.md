# 🎬 Which Movie Should I Watch?

Ever spent 30 minutes scrolling through streaming apps and ended up
watching nothing? This project fixes that.

Give it a year, and it instantly shows you the **Top 50 most popular
movies** of that year, ranked by IMDb votes, with ratings included.

## 💡 Why I built this

I'm a first-year IT student, and I wanted a project that solves a real,
everyday problem while teaching me how real-world data works:
downloading large datasets, cleaning them, filtering them and turning
raw numbers into something useful. It started as a BeautifulSoup
web-scraping idea. When IMDb blocked scraping, I learned to adapt and
switched to IMDb's official datasets. Real projects change direction
like that, and handling it is part of the learning.

## ✨ Features

- Top 50 movies for any year (defaults to the current year)
- Shows rating and number of votes
- Saves results to a CSV file

## 🛠️ Built with

- Python
- pandas
- IMDb Non-Commercial Datasets

## 🚀 How to run

```bash
git clone https://github.com/YOUR_USERNAME/imdb-top50-movies.git
cd imdb-top50-movies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python scraper.py 2024
```

Leave out the year to use the current year.

## 🔮 Future plans

- Filter by genre
- Simple web interface with Flask
- Search and compare across years

## 📄 Data source

Data courtesy of IMDb (https://developer.imdb.com/non-commercial-datasets/),
used for personal and non-commercial purposes only.