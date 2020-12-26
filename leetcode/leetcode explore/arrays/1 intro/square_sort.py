from typing import List

class Solution:
    def sortedSquares_slow(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in  range(n):
            nums[i] *= nums[i]
        return sorted(nums)

    def sortedSquares(self, nums):
        # Uses 2 pointers for +ve values 
        # and -ve values and converges to 0
        result = [0] * len(nums)
        l= 0
        r = len(nums)-1
        while l <= r:
            left = abs(nums[l])
            right = abs(nums[r])
            if left > right:
                result[r - l] = left * left
                l += 1
            else:
                result[r - l] = right * right
                r -= 1
        return result