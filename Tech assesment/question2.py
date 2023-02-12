def maxProfit(prices):
    if len(prices) < 2:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit

if __name__ == "__main__":
    prices = list(map(int, input("Enter the prices: ").strip().split()))
    n = len(prices)
    if n < 1 or n > 105:
        print("Invalid input: the number of prices should be between 1 and 105")
    else:
        for price in prices:
            if price < 0 or price > 104:
                print("Invalid input: each price should be between 0 and 104")
                break
        else:
            result = maxProfit(prices)
            print("The maximum profit that can be achieved is:", result)
