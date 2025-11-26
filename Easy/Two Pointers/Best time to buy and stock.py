from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        min_index = 0
        max_index = 0
        profit = 0
        while r < len(prices):
            if prices[r] < prices[min_index]:
                profit = max(profit, prices[max_index] - prices[min_index])
                min_index = r
                max_index = r
            if prices[r] > prices[max_index]:
                max_index = r
            r += 1
        profit = max(profit, prices[max_index] - prices[min_index])
        print(min_index, max_index)
        return profit
