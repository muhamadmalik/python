class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        l = 0 # buying 
        r = 1 # selling 
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return profit

prices = [7,1,5,3,6,4]

statement = Solution()
result = statement.maxProfit(prices)
print(result)