# Import scraper function
from scraper import scraper

# Our URL
URL = "https://www.hamropatro.com/gold"

# Destructure the gold price and silver price form the returned tuple
(gold_price, silver_price) = scraper(URL)

# Displaying the results
print(f"Gold price: {gold_price}")
print(f"Silver price: {silver_price}")
