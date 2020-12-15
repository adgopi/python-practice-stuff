from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        current_count = max_count = nums[0]
        for i in range(1,n):
            if nums[i] == 1:
                current_count = current_count + 1
            else:
                current_count = 0
            max_count = max(current_count, max_count)
        return max_count