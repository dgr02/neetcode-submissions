class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tracker1 = 0
        tracker2 = 1
        maxP = 0
        
        while tracker2 < len(prices):
            if prices[tracker1] < prices[tracker2]:
                profit = prices[tracker2] - prices[tracker1]
                maxP = max(maxP, profit)
            else:
                tracker1 = tracker2

            tracker2 += 1
        
        return maxP