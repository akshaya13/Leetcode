class Solution:
    def firstUniqChar(self, s: str) -> int:        
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # Step 2: Traverse the string to find the first unique character
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i  # Return the index of the first unique character
        
        return -1  # Return -1 if no unique character is found
