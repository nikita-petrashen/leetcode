class Solution:
    def maxProfit(self, prices):
        buy_price = prices[0]
        max_profit = 0
        for price in prices:
            profit = price - buy_price
            if profit > max_profit:
                max_profit = profit
            if price < buy_price:
                buy_price = price

        return max_profit


if __name__ == "__main__":
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))
