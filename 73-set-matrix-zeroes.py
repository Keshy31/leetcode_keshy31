import time


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print(matrix)


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

start_time = time.perf_counter_ns()

solution = Solution()
solution.setZeroes(matrix)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000

print(f"Elapsed time: {elapsed_time: .2f}ms")
