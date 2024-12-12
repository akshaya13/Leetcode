class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0  # Difference cannot be negative

        seen = set()
        unique_pairs = set()

        for num in nums:
            if num + k in seen:
                unique_pairs.add((num, num + k))
            if num - k in seen:
                unique_pairs.add((num - k, num))
            seen.add(num)

        return len(unique_pairs)