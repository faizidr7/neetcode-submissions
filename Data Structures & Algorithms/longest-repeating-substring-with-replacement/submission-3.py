class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        count = {}
        maxFreq = 0

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            maxFreq = max(count.values())
            if (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            else:
                result = (r - l + 1)
        result = max(result, r - l + 1)
        return result



        