import time


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
            return arr

        reverse(nums, 0, n - 1)
        print(nums)
        reverse(nums, 0, k - 1)
        print(nums)
        reverse(nums, k, n - 1)
        print(nums)


start_time = time.perf_counter_ns()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

solution = Solution()
solution.rotate(nums, k)
end_time = time.perf_counter_ns()

elapsed_time = (end_time - start_time) / 100000
print(f"Execution time: {elapsed_time:.2f} milliseconds")
