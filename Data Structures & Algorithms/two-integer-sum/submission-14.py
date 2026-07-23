class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 3, 4, 5, 6   target = 7
        # complement = target - num -> 7 -3 = 4 
        
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i