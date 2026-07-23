class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = []

        for i in range(len(nums)):
            product_var = 1
            for j in range(len(nums)):
                if i != j:
                    product_var *= nums[j]
            product.append(product_var)

        return product

