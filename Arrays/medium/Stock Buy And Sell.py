#Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction.
#If you cannot achieve any profit, return 0.

def buy_sell_stock(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price) 
        profit = price - min_price         
        max_profit = max(max_profit, profit) 

    return max_profit


arr=list(map(int,input().split()))
m=buy_sell_stock(arr)
print(m)
