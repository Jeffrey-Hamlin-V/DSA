from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = float("inf")
        maximum_profit = 0

        for price in prices:
            lowest_price = min(lowest_price, price)
            maximum_profit = max(maximum_profit, price - lowest_price)

        return maximum_profit
