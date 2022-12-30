from file_handling import get_data


def get_average() -> float:
    prices = get_data()

    sum_of_gold_price = 0
    sum_of_silver_price = 0

    for price in prices:
        gold_price, silver_price, _ = price.split(",")

        sum_of_gold_price += float(gold_price)
        sum_of_silver_price += float(silver_price)

    length = len(prices)

    average_gold_price = sum_of_gold_price / length
    average_silver_price = sum_of_silver_price / length

    return {
        average_gold_price: average_gold_price,
        average_silver_price: average_silver_price,
    }
