# Import scraper function
from scraper import scraper

# Import necessary functions
from file_handling import add_data, get_data
from statistics_ import get_average

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

# Get new prices fromt get_data function
new_prices = get_data()

print(f"\n{'='*10} This week's prices: {'='*10}\n")

# Iterate over each line and display the data
for price in new_prices:
    gold_price, silver_price, day = price.split(",")

    print(day.strip())
    print(f"Gold price   : {gold_price}")
    print(f"Silver price : {silver_price}\n")

# Display average
average_gold_price, average_silver_price = get_average()

print(f"\n{'='*10} Average prices: {'='*10}\n")
print(f"Average Gold price   : {average_gold_price}")
print(f"Average Silver price : {average_silver_price}\n")
