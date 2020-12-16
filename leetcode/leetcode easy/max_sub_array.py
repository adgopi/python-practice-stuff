from typing import List

class Solution:

    #greedy
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1,n):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum

    # def maxSubArray_dnc:

print(Solution.maxSubArray('', [-2,1,-3,4,-1,2,1,-5,4]))    #6
print(Solution.maxSubArray('', [1]))                        #1
print(Solution.maxSubArray('', [0]))                        #0
print(Solution.maxSubArray('', [-1]))                       #-1
print(Solution.maxSubArray('', [-2147483647]))              #-2147483647