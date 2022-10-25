class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # set left, right pointer
        res = 0
        left, right = 0, 1

        # to avoid out of bound error
        while right < len(prices):
            
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                res = max(res, profit)

            else:
                left = right
            
            right += 1
        
        return res