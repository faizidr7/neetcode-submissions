class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            complement = 0 - num
            while left < right:
                if (nums[left] + nums[right]) == complement:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                elif (nums[left] + nums[right]) < complement:
                    left += 1
                else:
                    right -= 1
        return result