class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # Initialize variables
        first_buy, profit1 = float('inf'), 0
        second_buy, profit2 = float('inf'), 0
        
        for price in prices:
            # For the first transaction: find the minimum price to buy and maximum profit
            first_buy = min(first_buy, price)
            profit1 = max(profit1, price - first_buy)
            
            # For the second transaction: find the minimum price to buy and maximum profit
            second_buy = min(second_buy, price - profit1)
            profit2 = max(profit2, price - second_buy)
        
        return profit2