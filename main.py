# Import termcolor to print colorful text on terminal
from termcolor import cprint

# Import the datetime module for working with dates
from datetime import datetime

# Import necessary functions
from scraper import scraper
from file_handling import add_data, get_data
from statistics_ import get_average

# Import URL
from constants import URL

# Pass the URL to the scraper function and store the returned prices
prices = scraper(URL)

# Displaying the results
cprint(f"\n{'='*10} Today's price: {'='*10}\n", "green")
cprint(f"Gold price   : {prices[0]}", "yellow")
cprint(f"Silver price : {prices[1]}\n", "blue")

# Add data to file
add_data(prices)

# Get new prices fromt get_data function
new_prices = get_data()

cprint(f"\n{'='*10} This week's prices: {'='*10}\n", "green")

# Iterate over each line and display the data
todays_day = datetime.now().strftime("%A")

for price in new_prices:
    gold_price, silver_price, day = price.split(",")

    day = day.strip()

    print(f"{day} (today)" if day == todays_day else day)
    cprint(f"Gold price   : {gold_price}", "yellow")
    cprint(f"Silver price : {silver_price}\n", "blue")

# Display average
average_gold_price, average_silver_price = get_average()

cprint(f"\n{'='*10} Average prices: {'='*10}\n", "green")
cprint(f"Average Gold price   : {average_gold_price:.2f}", "yellow")
cprint(f"Average Silver price : {average_silver_price:.2f}\n", "blue")
