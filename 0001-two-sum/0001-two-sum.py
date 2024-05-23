class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        PrevElementMap = {} # val : Index

        for i, n in enumerate(nums):
            diff = target - n
            
            if diff in PrevElementMap:
                return [PrevElementMap[diff], i]
            PrevElementMap[n] = i
        return
        