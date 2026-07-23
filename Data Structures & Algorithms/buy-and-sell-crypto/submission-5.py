class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        current_min = float("inf")
        max_profit = 0

        for i in range(len(prices)):

            if prices[i] < current_min:
                current_min = prices[i]
            else:
                current_profit = prices[i] - current_min
                max_profit = max(current_profit, max_profit)
        return max_profit
        
            
