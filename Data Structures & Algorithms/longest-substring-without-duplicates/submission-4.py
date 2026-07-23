class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # abca
        # a, ab, abc, bca

        charSet = set()
        max_longest = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])

            longest = (r - l + 1)

            max_longest = max(longest, max_longest)
        return max_longest
            
