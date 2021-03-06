class Solution:
    def get_first_non_repeating_character(self, s: str) -> int:

        # O(N^2) time, O(1) space
        # for i, ch in enumerate(s):
        #     if s.find(ch, i+1) == -1:
        #         return i
        # return -1

        # O(N) time and O(1) space because only 26 characters in alphabets
        char_map = {}
        for i, ch in enumerate(s):
            if ch in char_map:
                char_map[ch].append(i)
            else:
                char_map[ch] = [i]
        for ch in s:
            if len(char_map[ch]) == 1:
                return char_map[ch][0]
        return -1
        
# regarding python ordered and unorder dictionaries in newer python versions:
# http://gandenberger.org/2018/03/10/ordered-dicts-vs-ordereddict/#:~:text=Standard%20dict%20objects%20preserve%20order,makes%20the%20OrderedDict%20class%20obsolete
#
# O(N^2) time, O(1) space --> O(N) time, O(N) space (?) ---> actually O(N) time and O(1) space because only 26 characters in alphabets

