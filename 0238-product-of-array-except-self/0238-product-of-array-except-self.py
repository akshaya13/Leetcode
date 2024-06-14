class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums) #doesnt count in memory as per the problem
        #first pass
        prefix = 1 
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        #second pass - in reverse
        for i in range(len(nums) -1, -1, -1):
            result[i] *= postfix # multiply prefix and postfix in 2nd pass
            postfix *= nums[i]
        return result