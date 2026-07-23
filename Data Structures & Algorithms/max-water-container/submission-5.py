class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            min_height = min(heights[l], heights[r])
            length = r - l

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            curr_area = min_height * length
            
            max_area = max(curr_area, max_area)
        return max_area


        