class Solution:
    def frequencySort(self, s: str) -> str:
        scount = Counter(s)
        return ''.join(sorted(s, key = lambda x: (scount[x], x), reverse = True))