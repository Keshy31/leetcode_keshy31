import time


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = len(nums)

        while p1 < p2:
            print(f"{nums} index {p1} value: {nums[p1]}")
            if nums[p1] == 0:
                print("ping")
                nums.append(0)
                nums.pop(p1)
                p2 -= 1
            else:
                p1 += 1
        print(nums)


nums = [1, 2, 3, 0, 0, 0, 4, 0, 2, 0, 1, 2, 0, 0]

start_time = time.perf_counter_ns()
solution = Solution()
print(solution.moveZeroes(nums))
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000
print(f"Elapsed time: {elapsed_time:.2f}ms")
