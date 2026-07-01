class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n
        
        # Step 1: Calculate prefix products (left side)
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
            
        # Step 2: Calculate suffix products (right side) and multiply
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
            
        return result
