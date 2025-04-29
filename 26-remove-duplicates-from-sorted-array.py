class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pointer1 = 0
        pointer2 = 1

        while pointer2 < len(nums):
            if nums[pointer1] < nums[pointer2]:
                pointer1 += 1
                nums[pointer1] = nums[pointer2]
            pointer2 += 1
        return pointer1 + 1


nums = [1, 1, 2]

solution = Solution()
solution.removeDuplicates(nums)
