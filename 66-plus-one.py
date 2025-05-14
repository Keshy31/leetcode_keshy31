import time


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        largeIntString = "".join(str(x) for x in digits)
        largeInt = int(largeIntString) + 1
        return [int(x) for x in list(str(largeInt))]


digits = [0]

start_time = time.perf_counter_ns()
solution = Solution()
solution.plusOne(digits)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000
print(f"Elapsed time: {elapsed_time:.2f}ms")
