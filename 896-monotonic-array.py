import time


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True

        print(nums)

        increasing = True
        decreasing = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
            elif nums[i] < nums[i - 1]:
                increasing = False

            if not increasing and not decreasing:
                return False

        return True


nums = [1, 2, 2, 3]

start_time = time.perf_counter_ns()

solution = Solution()
solution.isMonotonic(nums)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000

print(f"Elapsed time: {elapsed_time: .2f}ms")
