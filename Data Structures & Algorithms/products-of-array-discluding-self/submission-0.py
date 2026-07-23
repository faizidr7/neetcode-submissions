class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product_nums = []

        for i, num in enumerate(nums):
            product_var = 1
            for j, num2 in enumerate(nums):
                if i != j:
                    product_var *= num2
            product_nums.append(product_var)

        return product_nums