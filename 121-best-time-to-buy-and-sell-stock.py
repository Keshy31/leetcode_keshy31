import time


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        print(prices)
        minPrice = prices[0]
        maxProfit = 0

        for i in range(1, len(prices), 1):
            if prices[i] < minPrice:
                minPrice = prices[i]

            profit = prices[i] - minPrice

            if profit > maxProfit:
                maxProfit = profit

        print("Max profit = " + str(maxProfit))
        return maxProfit


start_time = time.perf_counter_ns()

prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
solution.maxProfit(prices)

end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 1000000
print(f"Execution time: {elapsed_time:.4f} milliseconds")
