class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
            n = len(nums)
            ans = [0]*2*n

            for i in range(len(nums)):
                ans[i] = nums[i]
                ans[i+n] = nums[i]
            
            return ans