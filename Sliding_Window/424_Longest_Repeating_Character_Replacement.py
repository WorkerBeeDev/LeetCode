class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0
        count = {}

        for right in range(len(s)):

            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1

            cells_count = right - left + 1

            if cells_count - max(count.values()) <= k:
                res = max(res, cells_count)
            else:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

        return res