## Problem: Given a list of stock prices over a N days, find the best time to buy and sell stock
## to maximize profit. You are allowed to make only one transaction.

## Solution: If we graph stock prices, we can see that we need to find max(prices[i] - prices[i-k])
## where i represents a particular day.

def bestTime(prices):
    minPrice = float('inf')
    maxProfit = 0

    for i in range(prices):
        if prices[i] < minPrice:
            minPrice = prices[i]
        elif maxProfit < prices[i] - minPrice:
            maxProfit = prices[i] - minPrice
    
    return maxProfit

