class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        newNums = set(nums)
        longest = 0
        for num in newNums:
            if (num - 1) not in newNums:
                current = num
                length = 1
                while (current + 1) in newNums:
                    length += 1
                    current += 1
                longest = max(longest, length)
        return longest
            
       

        
