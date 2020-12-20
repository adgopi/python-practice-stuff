from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        '''
        Return if there exist 2 elements in arr such 
        that one element is twice the other
        '''
        if arr.count(0)==1:
            arr.remove(0)
        elif arr.count(0)>=2:
            return True        
        for i in range(len(arr)):
            if arr[i]*2 in arr[:i]+arr[i+1:]:
                return True
        return False

        
print(Solution.checkIfExist('',[3,1,7,11]))