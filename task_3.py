old_prices = [1000, -50, 300, 0, 500]
discount = 20

def process_prices(prices, discount_percent):
    processed_prices = []

    discount_multiplier = 1 - (discount_percent / 100)

    for price in prices:
        if price > 0:
             final_price = price * discount_multiplier
             processed_prices.append(round(final_price))
    return processed_prices

final_prices = process_prices(old_prices, discount)

print(f"Ціни: {final_prices}")