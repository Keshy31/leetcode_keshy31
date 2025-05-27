import time


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        print(prices)
        minPrice = prices[0]
        maxProfit = 0

        for i in range(1, len(prices), 1):
            if prices[i] > prices[i - 1]:
                print(f"profit is {prices[i] - prices[i - 1]}")
                maxProfit += prices[i] - prices[i - 1]

        print("Max profit = " + str(maxProfit))
        return maxProfit


start_time = time.perf_counter_ns()

prices = [1, 2, 3, 4, 5]
solution = Solution()
solution.maxProfit(prices)

end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 1000000
print(f"Execution time: {elapsed_time:.4f} milliseconds")
