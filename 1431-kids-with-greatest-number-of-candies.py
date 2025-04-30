import time


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        print(candies)
        return [True]


candies = [2, 3, 5, 1, 3]
extraCandies = 3

solution = Solution()

start_time = time.perf_counter_ns()
solution.kidsWithCandies(candies, extraCandies)
end_time = time.perf_counter_ns()

elapsed_time = (end_time - start_time) / 100000

print(f"Execution time: {elapsed_time:.3f} milliseconds")
