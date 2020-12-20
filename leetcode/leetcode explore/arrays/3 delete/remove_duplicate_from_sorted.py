from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Removes duplicates of all values present in a sorted list
        nums and returns final length of the list after all removals
        '''
        # O(N) time (O(N^2) time?), O(1) space
        # Note this does not actually remove the elements, but 
        # rearranges the array to place only 1 copy of each value
        # at the start of the array. 2 pointers are used for this.
        j = 0
        n = len(nums)
        for i in range(1,n):
            if nums[j] != nums[i]:
                nums[j+1] = nums[i]
                j += 1
        return j + 1
