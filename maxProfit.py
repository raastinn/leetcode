class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max = prices[0]
        difference = 0
        for i in range(1, len(prices)):
            if min > prices[i]:
                min = prices[i]
                max = prices[i]
            if max < prices[i]:
                max = prices[i]
            temp = max - min
            if difference < temp:
                difference = temp
        return difference
            
