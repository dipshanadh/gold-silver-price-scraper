# Import the datetime module for working with dates
from datetime import datetime

# Import file name
from constants import FILE_NAME


def add_data(prices: dict) -> None:
    # Get today's day
    todays_day = datetime.now().strftime("%A")

    # Destructure the gold price and silver price
    gold_price, silver_price = prices

    try:
        # Open the file for reading and writing mode
        file = open(FILE_NAME, "r+")

        # Read each lines
        file_content = file.readlines()

        # Get the last data and its day
        last_data = file_content[len(file_content) - 1]
        day_of_last = last_data.split(",")[2].strip()

        # Update the file if it is new data
        if todays_day != day_of_last:
            file.write(f"{gold_price},{silver_price},{todays_day}")
            file.write("\n")

        # Close the file
        file.close()

    except FileNotFoundError:
        print(f"\n{'='*10} Created data.txt file {'='*10}")

        # Create a new file in writing mode
        with open(FILE_NAME, "w") as file:
            file.write(f"{gold_price},{silver_price},{todays_day}")
            file.write("\n")


def get_data() -> list:
    # Open the file in reading mode
    with open(FILE_NAME, "r") as file:
        # Read each lines
        file_content = file.readlines()

        return file_content


def display_data() -> None:
    print(f"\n{'='*10} This week's prices: {'='*10}\n")

    # Get prices from the get_data funtion
    prices = get_data()

    # Iterate over each line and display the data
    for price in prices:
        gold_price, silver_price, day = price.split(",")
        print(day.strip())
        print(f"Gold price   : {gold_price}")
        print(f"Silver price : {silver_price}\n")
