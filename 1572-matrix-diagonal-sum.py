import time


class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        print(mat)
        sum = 0
        size = len(mat)
        for i in range(size):
            print(mat[i])

            if size % 2 == 0:
                sum += mat[i][i]
                sum += mat[i][len(mat) - i - 1]
            elif i == size // 2:
                sum += mat[i][i]
            else:
                sum += mat[i][i]
                sum += mat[i][len(mat) - i - 1]

        print(sum)

        return sum


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

solution = Solution()

start_time = time.perf_counter_ns()
solution.diagonalSum(mat)
end_time = time.perf_counter_ns()

elapsed_time = (end_time - start_time) / 100000

print(f"Execution time: {elapsed_time:.3f} milliseconds")
