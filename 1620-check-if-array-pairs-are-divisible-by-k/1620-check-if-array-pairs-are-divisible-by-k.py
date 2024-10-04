class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # Create a frequency array for remainders
        freq = [0] * k
        
        # Fill the frequency array
        for num in arr:
            remainder = ((num % k) + k) % k  # Handle negative numbers
            freq[remainder] += 1
        
        # Check the conditions for pairing
        for i in range(1, (k // 2) + 1):
            if i == k - i:  # Special case for the middle element when k is even
                if freq[i] % 2 != 0:  # Must have even count
                    return False
            else:
                if freq[i] != freq[k - i]:  # Count of i must match count of k-i
                    return False
        
        # Check for the zero remainder
        if freq[0] % 2 != 0:  # Must have even count
            return False
        
        return True
