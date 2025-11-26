from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices) - 1
        mi = prices[l]
        m = prices[r]
        while r > l:
            if prices[l] < mi:
                mi = prices[l]
            if prices[r] > m:
                m = prices[l]
            l += 1
            r -= 1
        profit = m-mi
        print(m, mi)
        if profit <= 0:
            return 0
        return profit