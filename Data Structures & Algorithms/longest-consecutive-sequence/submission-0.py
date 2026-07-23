class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums2 = set(nums)
        numCount = 0

        for num in nums2:
            if num - 1 not in nums2:
                length = 0
                while ((num + length) in nums2):
                    length += 1
                numCount = max(length, numCount)
        return numCount
        