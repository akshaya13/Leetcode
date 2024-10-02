class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        
        # Initialize result array with 1's
        result = [1] * length
        
        # First pass (Left to Right): Calculate prefix product on the fly
        prefix_product = 1
        for i in range(length):
            result[i] = prefix_product
            prefix_product *= nums[i]
        
        # Second pass (Right to Left): Calculate postfix product on the fly
        postfix_product = 1
        for i in range(length - 1, -1, -1):
            result[i] *= postfix_product
            postfix_product *= nums[i]
        
        return result
    