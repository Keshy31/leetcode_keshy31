class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        p = 0
        hashmap = {}

        while p < len(nums):
            hashmap[nums[p]] = hashmap.get(nums[p], 0) + 1
            if hashmap[nums[p]] > len(nums) / 2:
                return nums[p]
            p += 1

        return p


nums = [2]

solution = Solution()

solution.majorityElement(nums)
