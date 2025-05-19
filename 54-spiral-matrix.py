import time


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        print(matrix)
        p = [0, 0]
        m = len(matrix)
        print(f"m = {m}")

        n = len(matrix[0])
        print(f"n = {n}")

        for i in range(m * n):
            print(f"p --> {p} || value = {matrix[p[0]][p[1]]}")

            if p[0] == 0:
                p[1] += 1
            elif p[1] == 0:
                p[0] -= 1
            elif p[0] == m - 1:
                p[1] -= 1
            elif p[1] == n - 1:
                p[0] += 1

        return [1]


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

start_time = time.perf_counter_ns()

solution = Solution()
solution.spiralOrder(matrix)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000

print(f"Elapsed time: {elapsed_time: .2f}ms")
