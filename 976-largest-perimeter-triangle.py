class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums = sorted(nums, reverse=True)
        print(nums)
        result = 0
        for i in range(len(nums) - 2):
            a = nums[i]
            b = nums[i + 1]
            c = nums[i + 2]

            if (b + c) > a and (a + b + c) > result:
                result = a + b + c
            else:
                continue
        print(result)
        return result


nums = [3, 2, 3, 4]

solution = Solution()
solution.largestPerimeter(nums)
