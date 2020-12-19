from typing import List

class Solution:
    def merge_naive(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #O((m+n)log(m+n)) time, O(1) space. Avoid this.
        nums1[:] = sorted(nums1[:m] + nums2)

    def merge_from_start(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # O(m+n) time, O(m) space, uses 2 pointers and creates a 
        # copy of first list. Does not utilize that the arrays are 
        # already sorted

        nums1_copy = nums1[:m]
        nums1[:] = []
        i = j = 0

        while i < m and j < n :
            if nums2[j] < nums1_copy[i]:
                nums1.append(nums2[j])
                j += 1
            else:
                nums1.append(nums1_copy[i])
                i += 1

        if i < m :
            nums1[i+j:] = nums1_copy[i:]
        if j < n :
            nums1[i+j:] = nums2[j:]

    def merge_from_end(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # O(m+n) time, O(1) space, uses 3 pointers and fills array 
        # from end. Removes need for copy of nums1

        i = m - 1
        j = n - 1
        p = m + n - 1
        while i >= 0 and j >= 0 :
            if nums2[j] > nums1[i]:
                nums1[p] = nums2[j]
                j -= 1
            else:
                nums1[p] = nums1[i]
                i -= 1
            p -= 1
        nums1[:j + 1] = nums2[:j + 1]

