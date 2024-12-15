class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumMap = {0:1}
        res = 0
        curSum = 0
        

        for num in nums:
            curSum += num
            diff = curSum - k
            res += sumMap.get(diff, 0)
            sumMap[curSum] = 1 + sumMap.get(curSum, 0)
        
        return res

 