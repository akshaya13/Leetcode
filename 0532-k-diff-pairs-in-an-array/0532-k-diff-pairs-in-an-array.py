from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0  # Absolute difference cannot be negative
        
        freq = Counter(nums)
        count = 0
        
        if k == 0:
            # Count elements with frequency > 1 for k = 0
            for num in freq:
                if freq[num] > 1:
                    count += 1
        else:
            # Count pairs where num + k exists
            for num in freq:
                if num + k in freq:
                    count += 1
        
        return count