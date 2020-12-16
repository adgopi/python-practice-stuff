from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        while i < (m + n) or j < n:
            nums1.insert(i+j, min(nums1[i], nums2[j]))
            if nums2[j] < nums1[i]:
                j+=1
            else:
                i+=1
            nums1[:] = nums1[0:m+n]
