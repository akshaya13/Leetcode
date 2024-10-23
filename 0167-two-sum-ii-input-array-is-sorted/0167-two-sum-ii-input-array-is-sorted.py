class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap = {}

        for i,num in enumerate(numbers, start = 1):
            diff = target - num
            if diff in prevMap:
                return[prevMap[diff], i]
            prevMap[num]= i