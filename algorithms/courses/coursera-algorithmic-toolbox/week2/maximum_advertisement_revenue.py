def maximum_advertisement_revenue(prices, clicks):
    prices = sorted(prices)
    clicks = sorted(clicks)
    sum = 0
    for index in range(0, len(prices)):
        sum = sum + prices[index] * clicks[index]

    return sum