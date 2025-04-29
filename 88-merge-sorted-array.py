class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
       
        while p1 >= 0 and p2 >= 0:
            if (nums1[p1] > nums2[p2]):
                nums1[p] = nums1[p1]
                p -= 1
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1
        
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

# Input values
nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]         
n = 3

# Create an instance of the Solution class
solution = Solution()

#Call the merge method
solution.merge(nums1, m, nums2, n)
