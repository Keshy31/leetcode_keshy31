import time


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        print(digits)
        largeIntString = "".join(str(x) for x in digits)
        print(int(largeIntString) + 1)
        largeInt = int(largeIntString) + 1
        test = list(str(largeInt))
        print(test)

        return []


digits = [9]

start_time = time.perf_counter_ns()
solution = Solution()
solution.plusOne(digits)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000
print(f"Elapsed time: {elapsed_time:.2f}ms")
