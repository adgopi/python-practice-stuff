from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # First create a mapping for order of characters in the language
        # and their corresponding index/precedence in that language
        order_index = { c:i for i,c in enumerate(order)}
        
        # Then iterate over the list of words taking 2 adjacent words at a time
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            # Compare character to character till either a difference is found 
            # or we don't find a difference, i.e. the words are the same or there
            # is no difference and they are not of the same length
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if order_index[word1[j]] > order_index[word2[j]]:
                        return False
                    break
            # Note this else being used with the for if a break occurs!
            else:
                # if first word is longer than second word and no 
                # difference is found, the order is incorrect
                if len(word1) > len(word2):
                    return False

            # if no conditions are broken, return True
            return True


S = Solution()
print(S.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))