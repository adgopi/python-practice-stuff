from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        Remove all instances of val from nums. 
        '''
        # Using 2 pointers, one for traversing the list and one
        # for traversing elements of the list that are not the passed
        # val, we can replace the elements to be removed 
        j = 0
        for i in range(len(nums)): 
            if nums[i] != val: 
                nums[j] = nums[i] 
                j += 1
        return j

    def removeElementPython(self, nums: List[int], val: int) -> int:
        '''
        Same as removeElement but with using in built functions
        '''
        while True:
            try:
                nums.remove(val)
            except:
                break
        return len(nums)
