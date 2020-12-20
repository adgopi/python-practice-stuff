from typing import List

class Solution:
    def FizzBuzz(self, n: int) -> List[str]:
        # Note this implementation works since the order of the strings is 
        # defined and the numbers are in ascending order, resulting in easy 
        # calculation of common multiples.
        result = []
        for i in range(1,n+1):
            appendstring = ""
            if not i % 2:
                appendstring += "Coconut"
            if not i % 3:
                appendstring += "Fizz"
            if not i % 5:
                appendstring += "Buzz"
            if not appendstring:
                appendstring = str(i)
            result.append(appendstring)
        return result

S = Solution()
print(S.FizzBuzz(30))