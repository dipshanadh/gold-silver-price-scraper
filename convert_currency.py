# Helper function to convert string price (e.g. Nrs. 86,675.00) into number


def convert_currency(price_string: str) -> float:

    # At first, remove the whitespace, new line and the commas
    # Then select the price by separating the string by the space
    numeric_price = (
        price_string.strip().replace("\n", " ").replace(",", "").split(" ")[1]
    )

    return float(numeric_price)
