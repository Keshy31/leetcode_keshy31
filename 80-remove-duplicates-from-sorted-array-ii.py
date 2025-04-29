class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        p1 = 2
        p2 = 2

        while p2 < len(nums):
            if nums[p1 - 2] < nums[p2]:
                nums[p1] = nums[p2]
                p1 += 1
            p2 += 1
        return p1


nums = [1, 1, 1, 2, 2, 3]
solution = Solution()
solution.removeDuplicates(nums)
