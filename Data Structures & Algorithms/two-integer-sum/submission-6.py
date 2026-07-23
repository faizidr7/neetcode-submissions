class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        seen={}

        for i , num in enumerate(nums):
            t2= target - num

            if t2 in seen:
                return [seen[t2],i]
            
            seen[num]=i

    