class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in t:
            d[c] = d.get(c, 0) - 1
        return all(v == 0 for v in d.values())