class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary_s = {}
        dictionary_t = {}

        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))

        if len(sorted_s) != len(sorted_t):
            return False

        for c in sorted_s:
            dictionary_s[c] = dictionary_s.get(c, 0) + 1
        for c in sorted_t:
            dictionary_t[c] = dictionary_t.get(c, 0) + 1

        return dictionary_s == dictionary_t
