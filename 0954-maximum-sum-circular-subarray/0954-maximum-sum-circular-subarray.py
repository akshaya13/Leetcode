class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = nums[0]
        gmax = nums[0]
        curMin = nums[0]
        gmin = nums[0]
        total = nums[0]

        for num in nums[1:]:
            total += num
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            gmax  = max(gmax, curMax)
            gmin = min(gmin, curMin)
        

        final = total - gmin

        if gmax  < 0:
            return gmax 
    
        return max(gmax, final)