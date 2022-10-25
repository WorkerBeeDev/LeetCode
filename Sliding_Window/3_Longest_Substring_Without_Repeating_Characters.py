from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        d = defaultdict(int)

        left, right = 0, 0
        res = 0

        while right < len(s):

            d[s[right]] += 1
            
            # character repeats
            while d[s[right]] > 1:
                d[s[left]] -= 1 # must delete the left pointer value
                left += 1

            res = max(res, right-left+1)
            right += 1
        return res
        