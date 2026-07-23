class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        newSet = set(nums)
        numCount = 0

        for num in newSet:
            if num - 1 not in newSet:
                longest = 0
                while ((num + longest) in newSet):
                    longest += 1
                numCount = max(longest, numCount)
        return numCount
        