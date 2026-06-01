class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        initial = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < initial:
                initial = prices[i]
            temp = prices[i] - initial
            if temp > profit:
                profit = temp
        return profit