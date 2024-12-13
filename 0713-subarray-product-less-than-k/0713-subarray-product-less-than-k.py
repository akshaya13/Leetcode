class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        prod = 1
        count = 0
        for r in range(len(nums)):
            prod *= nums[r]
            while l <= r and prod >= k:
                prod = prod // nums[l]
                l += 1
            count += (r - l + 1)
        return count