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
