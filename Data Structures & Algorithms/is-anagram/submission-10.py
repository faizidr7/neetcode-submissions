class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        seen1 = {}
        seen2 = {}

        for ch in s:
            if ch in seen1:
                seen1[ch] += 1
            else:
                seen1[ch] = 1

        for ch in t:
            if ch in seen2:
                seen2[ch] += 1
            else:
                seen2[ch] = 1
    
        return seen1 == seen2
        