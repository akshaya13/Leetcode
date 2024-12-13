class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        res = s.split()

        if len(res) != len(pattern):
            return False
        patternMap = {}
        

        for i in range(len(pattern)):
            p = pattern[i]
            w = res[i]
            
            if p in patternMap:
                if patternMap[p] != w:
                    return False
            elif w in patternMap.values():
                return False
            else:
                patternMap[p] = w
        return True