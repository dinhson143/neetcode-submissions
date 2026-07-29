class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right = 1
        min_price = prices[0]
        max_profit = 0
        while right < len(prices):
            if prices[right] <= min_price:
                # buy
                min_price = min(prices[right], min_price)
                right += 1
            else:
                max_profit = max(max_profit, prices[right] - min_price)
                right += 1

        print(max_profit)
        return max_profit