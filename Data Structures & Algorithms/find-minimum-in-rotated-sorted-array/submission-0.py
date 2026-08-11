class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # if l < middle but r > middle, minimum is in second half
        # if l < middle AND r < middle, compare l and r to see 
        # which is more less, and minimum will be in the more less half

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


