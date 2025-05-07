import time


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0

        while p1 < len(nums):
            print(f"{nums} index {p1} value: {nums[p1]}")
            if nums[p1] != 0:
                nums[p2] = nums[p1]
                p2 += 1
                print(f"P2 is {p2}")
                p1 += 1
            else:
                nums[p1] = 0
                p1 += 1
        print(nums)


nums = [0, 1, 0, 3, 12]

start_time = time.perf_counter_ns()
solution = Solution()
print(solution.moveZeroes(nums))
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000
print(f"Elapsed time: {elapsed_time:.2f}ms")
