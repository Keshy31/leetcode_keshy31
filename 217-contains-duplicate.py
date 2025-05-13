class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        print(nums)
        if len(nums) <= 1:
            return False
        digitMap = {}

        for num in nums:
            digitMap[num] = digitMap.get(num, 0) + 1
            if digitMap[num] >= 2:
                print(True)
                return True
        return False


nums = [1]

solution = Solution()
solution.containsDuplicate(nums)
