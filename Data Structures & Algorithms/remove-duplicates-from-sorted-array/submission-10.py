class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n2 = sorted(set(nums))
        
        nums[:len(n2)]=n2
        return len(n2)