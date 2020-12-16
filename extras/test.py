from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ## O((n+m)log(n+m)), O(1) Lazy solution
        # nums1[:] = sorted(nums1[:m] + nums2)
        
        #
