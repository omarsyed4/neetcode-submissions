class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Start at the m index.
        ptr1 = m - 1
        
        # Start at the n index.
        ptr2 = n - 1

        # Start a pointer at the complete end of nums1. 
        back = m + n - 1

        # While both are not at 0
        while ptr2 >= 0:
            if ptr1 >= 0 and nums1[ptr1] >= nums2[ptr2]:
                nums1[back] = nums1[ptr1]
                ptr1 -= 1
                back -= 1
            else:
                nums1[back] = nums2[ptr2]
                ptr2 -= 1
                back -= 1
        
