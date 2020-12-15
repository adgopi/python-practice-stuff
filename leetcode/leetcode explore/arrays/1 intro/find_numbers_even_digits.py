from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        counter = 0 
        for i in range(n):
            digits = len(str(nums[i]))
            if digits % 2 == 0:
                counter = counter + 1
        return counter
