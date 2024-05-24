#######################################
# Time Complexity  = O(n)
# Space Complexity = O(1)
# buy low, sell high 
#check if Selling price is greater than cost price.
#    1 - 7 = -6 (Here SP-CP= LOSS), so just update the Right pointer
#    5 - 1 = 4  Here profit --> so find profit and update Max profit and update the Right pointer

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy = left, sell = right 
        l, r = 0, 1  # 0 and 1 are indices
        maxProfit = 0
        while r < len(prices): # iterating the list           
            if prices[l] < prices[r]:
                curProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit, curProfit)
            else: 
                l = r
            
            r += 1 

        return maxProfit
        