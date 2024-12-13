from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charmap = Counter(chars)
        res = 0
        # for char in chars:
        #     charmap[char] = charmap.get(char,0) + 1
        
        for word in words:
            wordmap = Counter(word)
            can_form = True
            for char in wordmap:
                if wordmap[char] > charmap[char]:
                    can_form = False
                    break        
            
            if can_form:
                res += len(word)
            
        return res