class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # Solution 1:
        # return Counter(s) == Counter(t) #hash map but just counts
        
        # #Solution 2:
        # return sorted(s) == sorted(t) -- Time - o(n log n) but memory - o(1)

        if len(s) == len(t):
            
            countS, countT = {}, {} # hashmap
            for i in range(len(s)):
                countS[s[i]] =  1 + countS.get(s[i],0)
                countT[t[i]] = countT.get(t[i],0) + 1
            return countS == countT
        return False


