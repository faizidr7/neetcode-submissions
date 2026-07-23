class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        max_length = 0

        for num in nums:
            if (num - 1) not in seen:
                curr_length = 1
                curr_num = num
                while (curr_num + 1) in seen:
                    curr_length += 1
                    curr_num += 1
                max_length = max(max_length, curr_length)
        return max_length
