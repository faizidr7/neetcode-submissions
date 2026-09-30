class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # s = "zxyzxyz"
        # l = z, zx, zxy, xyz

        charSet = set()
        max_length = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
        
            longest = (r - l + 1)
            max_length = max(longest, max_length)
        return max_length
        
                

            
                
        