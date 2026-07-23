class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest_sub = 0
        sub_string = ""

        for char in s:
            if char not in sub_string:
                sub_string += char
            else:
                index = sub_string.find(char)
                sub_string = sub_string[index + 1:] + char
            longest_sub = max(longest_sub, len(sub_string))
        return longest_sub