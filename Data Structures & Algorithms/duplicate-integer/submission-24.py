class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        ms=set(nums)

        if len(ms) != len(nums):
            return True
        else:
            return False
            