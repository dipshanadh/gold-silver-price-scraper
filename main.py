# Import scraper function
from scraper import scraper

# Import necessary functions fir file handling
from file_handling import add_data, display_data

# Import URL
from constants import URL

# Pass the URL to the scraper function and store the returned prices
prices = scraper(URL)

# Displaying the results
print(f"\n{'='*10} Today's price: {'='*10}\n")
print(f"Gold price   : {prices[0]}")
print(f"Silver price : {prices[1]}\n")

# Add data to file
add_data(prices)

# Displaying data
display_data()
