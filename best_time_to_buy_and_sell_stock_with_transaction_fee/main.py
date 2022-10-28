class Solution:
    def maxProfit(self, prices, fee):
        has_stock = [-prices[0] - fee]
        no_stock = [0]
        for i in range(1, len(prices)):
            has_stock_today = max(has_stock[-1], no_stock[-1] - fee - prices[i])
            no_stock_today = max(has_stock[-1] + prices[i], no_stock[-1])
            has_stock.append(has_stock_today)
            no_stock.append(no_stock_today)

        return max(has_stock[-1], no_stock[-1])


if __name__ == "__main__":
    sol = Solution()
    prices = [1,3,2,8,4,9]
    fee = 2
    print(sol.maxProfit(prices, fee))
    prices = [1, 3, 7, 5, 10, 3]
    fee = 3
    print(sol.maxProfit(prices, fee))
    prices = [1, 5, 9]
    fee = 2
    print(sol.maxProfit(prices, fee))
    prices = [9, 8, 7, 1, 2]
    fee = 3
    print(sol.maxProfit(prices, fee))
    prices = [4, 5, 2, 4, 3, 3, 1, 2, 5, 4]
    fee = 1
    print(sol.maxProfit(prices, fee))
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(sol.maxProfit(prices, fee))
    prices = [1, 1, 1, 3, 5, 2, 5, 4, 3, 2]
    fee = 4
    print(sol.maxProfit(prices, fee))
