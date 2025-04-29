class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        differences = {}
        for index, num in enumerate(nums):
            if num in differences:
                res = [differences[num], index]
                return res
            else:
                differences[target - num] = index



nums = [3,2,4]
target = 6


solution = Solution()
solution.twoSum(nums, target)

