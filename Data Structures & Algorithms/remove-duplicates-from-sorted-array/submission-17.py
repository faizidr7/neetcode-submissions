class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
       s2 = sorted(set(nums))
       nums[:len(s2)]=s2

       return len(s2)