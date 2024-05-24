class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}  # key: value

        for i, n in enumerate(nums):
            if n in hashmap:
                j = hashmap[n]
                if abs(i - j) <= k:
                    return True
            # Always update the hashmap with the current index
            hashmap[n] = i

        return False
