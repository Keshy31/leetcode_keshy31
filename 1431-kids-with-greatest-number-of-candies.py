import time


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        max = 0

        for i in range(0, len(candies), 1):
            if candies[i] > max:
                max = candies[i]

        for i in range(0, len(candies), 1):
            if candies[i] + extraCandies >= max:
                result.append(True)
            else:
                result.append(False)

        print(result)
        return result


candies = [2, 3, 5, 1, 3]
extraCandies = 3

solution = Solution()

start_time = time.perf_counter_ns()
solution.kidsWithCandies(candies, extraCandies)
end_time = time.perf_counter_ns()

elapsed_time = (end_time - start_time) / 100000

print(f"Execution time: {elapsed_time:.3f} milliseconds")
