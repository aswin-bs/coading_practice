'''121. Best Time to Buy and Sell Stock
Solved
Easy
Topics
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , 1
        mp = 0
        
        while r < len(prices):

            if prices[l] < prices[r]:

                profit = prices[r] - prices[l]
                mp = max(profit , mp)
            else:
                l = r
            
            r+=1
        return mp
        