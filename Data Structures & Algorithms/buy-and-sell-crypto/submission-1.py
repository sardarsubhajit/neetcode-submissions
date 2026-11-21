class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, maxprofit = prices[0], 0   # initializing the buy price, and maxprofit
        for i in range(1, len(prices)):
            sell = prices[i]
            profit = sell - buy # for everyday we are looking for the profit amount
            if profit > 0:  # if profit is positive
                if maxprofit < profit:  # and more than last maxprofit then update it
                    maxprofit = profit
            else:   # incase of negative profit update the buy value
            
                buy = sell

        return maxprofit    