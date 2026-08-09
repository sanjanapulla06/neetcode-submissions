class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, sold, rest = -prices[0], 0, 0
        for i in range(1, len(prices)):
            prevHold, prevSold, prevRest = hold, sold, rest
            hold = max(prevHold, prevRest - prices[i])
            sold = prevHold + prices[i]
            rest = max(prevRest, prevSold)
        return max(sold, rest)