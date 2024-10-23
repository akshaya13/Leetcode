class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # prevMap = {}

        # for i,num in enumerate(numbers, start = 1):
        #     diff = target - num
        #     if diff in prevMap:
        #         return[prevMap[diff], i]
        #     prevMap[num]= i
        left = 0                   # Start pointer
        right = len(numbers) - 1   # End pointer
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]  # Convert to 1-indexed
            elif current_sum < target:
                left += 1  # Move left pointer to the right
            else:
                right -= 1  # Move right pointer to the left

        return []