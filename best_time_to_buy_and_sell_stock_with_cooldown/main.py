class Solution:
    def maxProfit(self, prices):
        has_stock = [0, -prices[0]]
        no_stock = [0, 0]
        for i in range(1, len(prices)):
            has_stock_today = max(has_stock[-1], no_stock[-2] - prices[i])
            no_stock_today = max(has_stock[-1] + prices[i], no_stock[-1])
            has_stock.append(has_stock_today)
            no_stock.append(no_stock_today)

        return max(has_stock[-1], no_stock[-1])


if __name__ == "__main__":
    sol = Solution()
    prices = [1,2,3,0,2]
    print(sol.maxProfit(prices))
