import time


class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        print(f"Original: {arr}")
        arr.sort()
        print(f"Ascending: {arr}")

        delta = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if (arr[i] - arr[i - 1]) != delta:
                return False
        return True


arr = [3, 5, 1]

start_time = time.perf_counter_ns()

solution = Solution()
solution.canMakeArithmeticProgression(arr)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000

print(f"Elapsed time: {elapsed_time: .2f}ms")
