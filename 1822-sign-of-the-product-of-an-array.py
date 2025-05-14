import time


class Solution:
    def arraySign(self, nums: list[int]) -> int:
        print(nums)

        result = 1

        for number in nums:
            if number == 0:
                return 0
            elif number < 0:
                result *= -1
        print(result)
        return result


nums = [-1, 1, -1, 1, -1]

start_time = time.perf_counter_ns()

solution = Solution()
solution.arraySign(nums)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000

print(f"Elapsed time: {elapsed_time: .2f}ms")
