class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #store first stock as variable

        maxprofit = 0
        buy = 0
        sell = 1

        while(sell < len(prices)):
            currentprofit = prices[sell] - prices[buy]

            if(prices[sell] > prices[buy]):
                maxprofit = max(currentprofit,maxprofit)
            else:
                buy = sell
            
            sell += 1

        return maxprofit

