class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buying = 0
        selling = 1
        
        max_profit = 0
        
        while selling < len(prices):
            if prices[selling] > prices[buying]:
                profit = prices[selling] - prices[buying]
                max_profit = max(max_profit, profit)
            else:
                buying = selling
            selling += 1
        
        return max_profit

prices = [10,1,5,6,7,1]

statement = Solution()
result = statement.maxProfit(prices)
print(result)