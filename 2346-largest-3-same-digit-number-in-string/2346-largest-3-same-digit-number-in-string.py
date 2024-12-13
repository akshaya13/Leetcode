class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        res = ""

        for i in range(len(nums) - 2):
            if nums[i] == nums[i+1] == nums[i+2]:
                res = max(res, nums[i: i+3])
        
        return res
