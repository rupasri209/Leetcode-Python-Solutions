"""
PROBLEM LINK: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if(buy_price > prices[i]):
                buy_price = prices[i]
            profit = max(profit, prices[i] - buy_price)
        return profit
        