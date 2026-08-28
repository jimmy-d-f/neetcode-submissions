class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary_s = {}
        dictionary_t = {}

        s = sorted(s)
        t = sorted(t)

        return s == t
