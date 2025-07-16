#Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction.
#If you cannot achieve any profit, return 0.

def buy_sell_stock(arr):
    mi=min(arr)
    m=float("inf")
    for i in range(len(arr)):
        ma=max(arr[i:])
        if ma>mi and mi in arr[i:]:
            m=min(ma-mi,m)


    return m







arr=list(map(int,input().split()))
m=buy_sell_stock(arr)
print(m)
