class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        print(nums)
        for i in range(len(nums) - 2):
            a = nums[i]
            b = nums[i + 1]
            c = nums[i + 2]

            if (b + c) > a and (a + b + c):
                return a + b + c
            else:
                continue
        return 0


nums = [3, 2, 3, 4]

solution = Solution()
solution.largestPerimeter(nums)
