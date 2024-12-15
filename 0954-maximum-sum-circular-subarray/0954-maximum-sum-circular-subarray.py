class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
      # Helper function to find the maximum subarray sum using Kadane's algorithm
        def kadane(nums):
            curMax = nums[0]
            maxSoFar = nums[0]
            curMin = nums[0]
            minsofar = nums[0]

            for num in nums[1:]:
                curMax = max(curMax + num, num)
                curMin = min(curMin + num, num)
                maxSoFar = max(maxSoFar, curMax)
                minsofar = min(minsofar, curMin)
            return maxSoFar, minsofar

        # Total sum of the array
        totalSum = sum(nums)

        # Maximum subarray sum (non-circular case)
        maxSum, minsum = kadane(nums)

        final = totalSum - minsum
        if maxSum < 0:
            return maxSum

        # Return the maximum of non-circular and circular cases
        return max(maxSum, final)