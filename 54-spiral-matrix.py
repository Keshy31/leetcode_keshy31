import time


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        print(matrix)
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])
        result = []

        while top < bottom and left < right:
            for i in range(right - left):
                result.append(matrix[top][left + i])
                print(result)
            top += 1

            for i in range(bottom - top):
                result.append(matrix[top + i][right - 1])
                print(result)
            right -= 1

            if top < bottom:
                for i in range(right - left):
                    result.append(matrix[bottom - 1][right - 1 - i])
                    print(result)
                bottom -= 1
            if left < right:
                for i in range(bottom - top):
                    result.append(matrix[bottom - 1 + i][left])
                    print(result)
                left += 1

        return result


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

start_time = time.perf_counter_ns()

solution = Solution()
solution.spiralOrder(matrix)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000

print(f"Elapsed time: {elapsed_time: .2f}ms")
