# Import requests to fetch the webpage
import requests

# Import BeautifulSoup to scrape the page
from bs4 import BeautifulSoup

# convert_currency helper function
from convert_currency import convert_currency


def scraper(URL: str) -> tuple:
    # Get the page
    response = requests.get(URL)

    # Prase the string to HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the parent list element of the price list
    list = soup.find(
        class_="gold-silver",
    )

    # Select the prices from the list
    prices = list.select("li:nth-child(even)")

    # Get the gold price & silver price
    gold_price = convert_currency(prices[1].text)
    silver_price = convert_currency(prices[2].text)

    # Return in dictionary form
    return (gold_price, silver_price)
